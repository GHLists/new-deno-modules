#!/usr/bin/env python3
"""Fetch modules newly published to JSR, the package registry of the Deno team.

JSR has no "recently created" feed. Instead the full package sitemap at
``https://jsr.io/sitemap-packages.xml`` is downloaded each run and diffed
against the previous run's baseline, and every unseen package is checked
against the [JSR API](https://api.jsr.io/scopes/<scope>/packages/<name>),
whose ``createdAt`` timestamp decides whether the module was created inside
the requested window.

The baseline of known packages is stored as a compressed text file in the
repo so the next run resumes from the previous state.
"""

import argparse
import csv
import datetime as dt
import http.client
import json
import lzma
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SITEMAP_URL = "https://jsr.io/sitemap-packages.xml"
PACKAGE_API_URL = "https://api.jsr.io/scopes/{scope}/packages/{name}"
DEFAULT_USER_AGENT = (
    "new-deno-modules/1.0 (https://github.com/GHLists/new-deno-modules)"
)

DESCRIPTION_LIMIT = 300
BASELINE_LIMIT = 300_000
CSV_HEADER = (
    "created_at",
    "package",
    "version",
    "score",
    "description",
)
BASELINE_SUFFIX = ".txt.lzma"

TRANSIENT_ERRORS = (
    urllib.error.URLError,
    TimeoutError,
    json.JSONDecodeError,
    http.client.HTTPException,
    OSError,
)


class NotFound(Exception):
    pass


def iso(moment):
    moment = moment.astimezone(dt.timezone.utc)
    if moment.microsecond:
        fraction = f"{moment.microsecond:06d}".rstrip("0")
        return moment.strftime("%Y-%m-%dT%H:%M:%S") + f".{fraction}Z"
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp(value):
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=dt.timezone.utc)
    return moment.astimezone(dt.timezone.utc)


def timestamp_filename(moment):
    moment = moment.astimezone(dt.timezone.utc)
    stamp = moment.strftime("%Y-%m-%dT%H-%M-%S")
    if moment.microsecond:
        stamp += "-" + f"{moment.microsecond:06d}".rstrip("0")
    return stamp + "Z"


def fetch_request(url, user_agent, accept, retries=3, backoff=5.0):
    last_error = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url, headers={"User-Agent": user_agent, "Accept": accept}
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise NotFound(url) from error
            last_error = error
        except TRANSIENT_ERRORS as error:
            last_error = error
        if attempt < retries:
            print(f"attempt {attempt} failed ({last_error}), retrying", file=sys.stderr)
            time.sleep(backoff * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def fetch_sitemap(user_agent, retries):
    text = fetch_request(
        SITEMAP_URL, user_agent, "application/xml", retries=retries
    ).decode("utf-8")
    root = ET.fromstring(text)
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    names = set()
    for element in root.findall(f"{namespace}url"):
        loc = element.findtext(f"{namespace}loc")
        if not loc:
            continue
        path = urllib.parse.urlparse(loc).path.lstrip("/")
        if path.startswith("@") and "/" in path:
            names.add(path[1:])
    if not names:
        raise RuntimeError("JSR sitemap contained no packages")
    return names


def clean_text(value, limit=DESCRIPTION_LIMIT):
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "\u2026"
    return text


def build_row(package, info):
    score = info.get("score")
    return {
        "created_at": iso(parse_timestamp(info["createdAt"])),
        "package": package,
        "version": clean_text(info.get("latestVersion"), 20),
        "score": score if isinstance(score, (int, float)) else "",
        "description": clean_text(info.get("description")),
    }


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def baseline_path(output_dir, manifest):
    stored = manifest.get("baseline", {}).get("path")
    if stored:
        return Path(stored)
    return Path(output_dir) / f"deno-modules-baseline{BASELINE_SUFFIX}"


def read_baseline_text(path):
    """Read the baseline from disk, or fall back to the committed copy.

    The workflow checks out only ``scripts`` from the repository, so the
    baseline can be missing from the working tree even though it is committed.
    """
    try:
        return lzma.decompress(path.read_bytes()).decode("utf-8")
    except (OSError, lzma.LZMAError):
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{path.as_posix()}"],
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    try:
        return lzma.decompress(result.stdout).decode("utf-8")
    except lzma.LZMAError:
        return None


def load_baseline(path):
    text = read_baseline_text(path)
    if text is None:
        return None
    return {line for line in text.splitlines() if line}


def save_baseline(path, names):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    blob = lzma.compress(("\n".join(sorted(names)) + "\n").encode("utf-8"))
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_bytes(blob)
    os.replace(temporary, path)


def read_manifest_text(path):
    """Read the manifest from disk, or fall back to the committed copy."""
    manifest_path = Path(path)
    try:
        return manifest_path.read_text(encoding="utf-8")
    except OSError:
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{manifest_path.as_posix()}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def load_manifest(path):
    text = read_manifest_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"manifest {path} is not valid JSON") from error
    if not isinstance(data, dict):
        raise RuntimeError(f"manifest {path} must contain a JSON object")
    version = data.get("state_version", 1)
    if version != 1:
        raise RuntimeError(f"manifest {path} has an unsupported state version")
    return data


def save_manifest(path, manifest):
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = manifest_path.with_name(f".{manifest_path.name}.tmp")
    text = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, manifest_path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="UTC start timestamp as ISO 8601 (default: end of the last list)",
    )
    parser.add_argument(
        "--until",
        help="UTC end timestamp as ISO 8601 (default: now)",
    )
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--manifest", default="latest.json")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--lookback-hours",
        type=float,
        default=1.0,
        help="window length when no previous list exists (default: 1)",
    )
    parser.add_argument(
        "--api-delay",
        type=float,
        default=0.2,
        help="seconds between JSR API requests (default: 0.2)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    until = parse_timestamp(args.until) if args.until else now
    manifest = load_manifest(args.manifest)

    if args.since:
        since = parse_timestamp(args.since)
        if "window" in manifest:
            stored_window = parse_timestamp(manifest["window"])
            if since < stored_window:
                raise RuntimeError(
                    "backfill would move the window backwards; "
                    f"the manifest window is {iso(stored_window)}"
                )
    elif "window" in manifest:
        since = parse_timestamp(manifest["window"])
    else:
        since = until - dt.timedelta(hours=args.lookback_hours)

    packages = fetch_sitemap(args.user_agent, args.retries)
    if len(packages) > BASELINE_LIMIT:
        raise RuntimeError(f"JSR sitemap grew beyond {BASELINE_LIMIT} packages")

    output = baseline_path(args.output_dir, manifest)
    known = load_baseline(output)
    if known is None:
        save_baseline(output, packages)
        manifest["baseline"] = {
            "path": output.as_posix(),
            "count": len(packages),
        }
        manifest["window"] = iso(until)
        manifest["source_truncated"] = False
        save_manifest(args.manifest, manifest)
        print(
            f"seeded baseline with {len(packages)} packages; "
            "next runs produce the first list"
        )
        return 0

    fresh = packages - known
    rows = []
    skipped = 0
    for package in sorted(fresh):
        scope, _, name = package.partition("/")
        url = PACKAGE_API_URL.format(
            scope=urllib.parse.quote(scope, safe=""),
            name=urllib.parse.quote(name, safe=""),
        )
        try:
            info = json.loads(
                fetch_request(
                    url, args.user_agent, "application/json", retries=args.retries
                )
            )
        except NotFound:
            skipped += 1
            continue
        try:
            created = parse_timestamp(info["createdAt"])
        except (KeyError, TypeError, ValueError):
            skipped += 1
            continue
        if created <= since or created > until:
            continue
        rows.append(build_row(package, info))
        time.sleep(args.api_delay)
    if skipped:
        print(f"skipped {skipped} packages without API data", file=sys.stderr)
    rows.sort(key=lambda row: row["created_at"])

    save_baseline(output, packages)
    manifest["baseline"] = {
        "path": output.as_posix(),
        "count": len(packages),
    }
    manifest["window"] = iso(until)
    manifest["source_truncated"] = False
    if rows:
        output_csv = (
            Path(args.output_dir)
            / f"new-deno-modules-{timestamp_filename(until)}.csv"
        )
        write_csv(output_csv, rows)
        manifest["list"] = {
            "path": output_csv.as_posix(),
            "from": iso(since),
            "to": iso(until),
            "count": len(rows),
        }
        print(
            f"wrote {len(rows)} modules created between {iso(since)} "
            f"and {iso(until)} to {output_csv}"
        )
    else:
        print(f"no new modules between {iso(since)} and {iso(until)}")
    save_manifest(args.manifest, manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
