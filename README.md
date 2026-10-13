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

## Latest list — 2026-10-13 15:23 UTC

New modules created between 2026-10-13 14:21 UTC and 2026-10-13 15:23 UTC.

[Full CSV](data/new-deno-modules-2026-10-13T15-23-18-630711Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-13 15:08:49 | [ende/std](https://jsr.io/ende/std) |  |  |  |
| 2026-10-13 15:17:19 | [primp/primp](https://jsr.io/primp/primp) |  |  |  |
| 2026-10-13 15:17:25 | [primp/vue](https://jsr.io/primp/vue) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
