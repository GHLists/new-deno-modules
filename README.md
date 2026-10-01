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

## Latest list — 2026-10-01 17:20 UTC

New modules created between 2026-10-01 16:21 UTC and 2026-10-01 17:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-01T17-20-51-488036Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-01 16:27:34 | [mrprolopstar/prodcalendar](https://jsr.io/mrprolopstar/prodcalendar) | 0.1.2 | 88 |  |
| 2026-10-01 16:30:18 | [timmo001/effect-ha](https://jsr.io/timmo001/effect-ha) | 0.1.0 | 52 |  |
| 2026-10-01 16:30:57 | [timmo001/effect-ha-bridge](https://jsr.io/timmo001/effect-ha-bridge) | 0.1.0 | 52 |  |
| 2026-10-01 17:18:32 | [hooksmith/html](https://jsr.io/hooksmith/html) |  |  | HTML parsing and metadata extraction utilities for Hooksmith |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
