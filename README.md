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

## Latest list — 2026-10-12 10:21 UTC

New modules created between 2026-10-12 09:22 UTC and 2026-10-12 10:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-12T10-21-33-219576Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-12 09:48:14 | [notusinggithub/wan27](https://jsr.io/notusinggithub/wan27) | 0.1.0 | 82 |  |
| 2026-10-12 09:50:02 | [zuke/apple](https://jsr.io/zuke/apple) | 1.0.0 | 100 | Typed wrappers for Apple’s signing tools in Zuke builds: CodesignTasks (codesig… |
| 2026-10-12 09:50:52 | [zuke/homebrew](https://jsr.io/zuke/homebrew) |  |  | Ship binaries through a Homebrew tap from a Zuke build: typed BrewTasks for the… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
