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

## Latest list — 2026-10-17 06:20 UTC

New modules created between 2026-10-17 05:19 UTC and 2026-10-17 06:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-17T06-20-36-967234Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-17 05:31:47 | [ende/front-matter](https://jsr.io/ende/front-matter) | 2026.10.15 | 94 | Extract front matter from strings |
| 2026-10-17 05:36:48 | [ende/fs](https://jsr.io/ende/fs) | 2026.10.15 | 88 | Helpers for working with the file system |
| 2026-10-17 05:39:01 | [ende/html](https://jsr.io/ende/html) | 2026.10.15 | 94 | Functions for HTML, such as escaping or unescaping HTML entities. |
| 2026-10-17 05:40:14 | [ende/media-types](https://jsr.io/ende/media-types) |  |  |  |
| 2026-10-17 06:15:05 | [prosubodh/laghu](https://jsr.io/prosubodh/laghu) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
