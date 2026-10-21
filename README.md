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

## Latest list — 2026-10-21 09:23 UTC

New modules created between 2026-10-21 08:19 UTC and 2026-10-21 09:23 UTC.

[Full CSV](data/new-deno-modules-2026-10-21T09-23-15-932547Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-21 08:47:39 | [tancky/upscale-calculator](https://jsr.io/tancky/upscale-calculator) | 0.1.1 | 100 | Dependency-free helpers for image upscaling math: scale factors (2x, 4x, 6x), t… |
| 2026-10-21 08:48:23 | [fjavierv/database-model](https://jsr.io/fjavierv/database-model) | 5.0.4 | 52 |  |
| 2026-10-21 09:00:34 | [paluigi/jsindexnum](https://jsr.io/paluigi/jsindexnum) |  |  | Package to compute index numbers |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
