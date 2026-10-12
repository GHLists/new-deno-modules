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

## Latest list — 2026-10-12 16:19 UTC

New modules created between 2026-10-12 15:18 UTC and 2026-10-12 16:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-12T16-19-16-286632Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-12 15:54:53 | [zuke/chocolatey](https://jsr.io/zuke/chocolatey) |  |  | Ship a prebuilt Windows binary through Chocolatey from a Zuke build: a typed ch… |
| 2026-10-12 15:55:45 | [zuke/signpath](https://jsr.io/zuke/signpath) |  |  | Authenticode signing through SignPath for Zuke builds: submit a signing request… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
