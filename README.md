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

## Latest list — 2026-10-21 08:19 UTC

New modules created between 2026-10-21 07:19 UTC and 2026-10-21 08:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-21T08-19-45-23854Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-21 07:25:52 | [binette/core](https://jsr.io/binette/core) | 0.1.0 | 88 |  |
| 2026-10-21 07:26:19 | [binette/scene](https://jsr.io/binette/scene) | 0.1.0 | 88 |  |
| 2026-10-21 07:26:44 | [binette/coulisses](https://jsr.io/binette/coulisses) | 0.1.0 | 88 |  |
| 2026-10-21 08:01:15 | [fjavierv/postgresql-migrations-ts](https://jsr.io/fjavierv/postgresql-migrations-ts) | 3.0.2 | 47 |  |
| 2026-10-21 08:05:56 | [imdevil/lotto432](https://jsr.io/imdevil/lotto432) | 1.0.0 | 52 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
