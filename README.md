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

## Latest list — 2026-11-06 06:20 UTC

New modules created between 2026-11-06 05:19 UTC and 2026-11-06 06:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-06T06-20-14-969774Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-06 05:42:30 | [helocore/sprite](https://jsr.io/helocore/sprite) |  |  |  |
| 2026-11-06 05:52:56 | [helocore/switch](https://jsr.io/helocore/switch) | 1.0.1 | 100 | Programmatic client for the Aethra Switch signed REST API — call Helocore egres… |
| 2026-11-06 05:59:54 | [leonidalekseev/domains-checker](https://jsr.io/leonidalekseev/domains-checker) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
