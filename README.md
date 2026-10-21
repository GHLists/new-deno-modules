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

## Latest list — 2026-10-21 14:23 UTC

New modules created between 2026-10-21 13:19 UTC and 2026-10-21 14:23 UTC.

[Full CSV](data/new-deno-modules-2026-10-21T14-23-13-667608Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-21 13:48:05 | [tab/linets](https://jsr.io/tab/linets) | 3.5.1 | 58 |  |
| 2026-10-21 13:58:24 | [tab/loose-types](https://jsr.io/tab/loose-types) | 1.0.1 | 76 |  |
| 2026-10-21 14:00:13 | [tab/linets-types](https://jsr.io/tab/linets-types) | 3.5.0 | 41 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
