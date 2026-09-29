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

## Latest list — 2026-09-29 06:20 UTC

New modules created between 2026-09-29 05:20 UTC and 2026-09-29 06:20 UTC.

[Full CSV](data/new-deno-modules-2026-09-29T06-20-25-953304Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-09-29 05:29:52 | [manojgowdain/ssdiskdb](https://jsr.io/manojgowdain/ssdiskdb) |  |  |  |
| 2026-09-29 05:38:22 | [sabilmurti/amneshia](https://jsr.io/sabilmurti/amneshia) | 3.0.2 | 100 | Deterministic, Git-Native Knowledge Graph & Truth Maintenance Engine for AI Age… |
| 2026-09-29 06:00:56 | [nodef/extra-array-view](https://jsr.io/nodef/extra-array-view) | 1.2.0 | 100 | An array view is a proxy to an underlying array. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
