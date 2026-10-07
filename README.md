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

## Latest list — 2026-10-07 09:20 UTC

New modules created between 2026-10-07 08:20 UTC and 2026-10-07 09:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-07T09-20-38-261231Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-07 08:40:31 | [zuke/aws](https://jsr.io/zuke/aws) |  |  | Typed AWS CLI wrapper for Zuke builds: every aws service command through one se… |
| 2026-10-07 08:41:11 | [zuke/az](https://jsr.io/zuke/az) |  |  | Typed Azure CLI wrapper for Zuke builds: every az command group through one set… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
