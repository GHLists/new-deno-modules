# New Deno modules

Hourly lists of modules newly published to
[JSR](https://jsr.io/), the package registry built by the Deno team and the
successor to [deno.land/x](https://deno.land/x). JSR has no "recently created"
feed, so the list is built by diffing the registry's full
[package sitemap](https://jsr.io/sitemap-packages.xml) against the previous
run and verifying each unseen package's ``createdAt`` timestamp through the
[JSR API](https://jsr.io/docs/api).
A GitHub Actions workflow runs every hour, fetches the modules created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-deno-modules-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-31 13:19 UTC

New modules created between 2026-10-31 12:18 UTC and 2026-10-31 13:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-31T13-19-46-503273Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-31 12:34:31 | [fitv/fitv](https://jsr.io/fitv/fitv) |  |  |  |
| 2026-10-31 12:35:19 | [fitv/freeimagetovideo](https://jsr.io/fitv/freeimagetovideo) | 0.1.0 | 64 |  |
| 2026-10-31 12:37:42 | [leonidalekseev/git-repo-cleaner](https://jsr.io/leonidalekseev/git-repo-cleaner) | 0.1.0 | 100 | Interactive CLI that removes AI-assistant artifacts (Claude Code, Cursor, Copil… |
| 2026-10-31 12:49:09 | [g9wp/dom-utils](https://jsr.io/g9wp/dom-utils) | 0.1.0 | 94 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
