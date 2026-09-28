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

## Latest list — 2026-09-28 10:26 UTC

New modules created between 2026-09-28 09:19 UTC and 2026-09-28 10:26 UTC.

[Full CSV](data/new-deno-modules-2026-09-28T10-26-12-183299Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-09-28 09:21:36 | [hyapi/plugin-rate-limit](https://jsr.io/hyapi/plugin-rate-limit) |  |  |  |
| 2026-09-28 09:24:04 | [hyapi/plugin-cors](https://jsr.io/hyapi/plugin-cors) |  |  |  |
| 2026-09-28 09:24:18 | [hyapi/plugin-csrf](https://jsr.io/hyapi/plugin-csrf) |  |  |  |
| 2026-09-28 09:24:26 | [hyapi/plugin-oidc](https://jsr.io/hyapi/plugin-oidc) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
