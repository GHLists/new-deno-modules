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

## Latest list — 2026-10-09 19:21 UTC

New modules created between 2026-10-09 18:18 UTC and 2026-10-09 19:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-09T19-21-07-191966Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-09 19:11:22 | [wildboar/pkinit](https://jsr.io/wildboar/pkinit) |  |  |  |
| 2026-10-09 19:11:57 | [wildboar/p772](https://jsr.io/wildboar/p772) |  |  |  |
| 2026-10-09 19:12:16 | [wildboar/sgp32](https://jsr.io/wildboar/sgp32) |  |  |  |
| 2026-10-09 19:13:23 | [wildboar/nist-csor](https://jsr.io/wildboar/nist-csor) |  |  |  |
| 2026-10-09 19:14:10 | [wildboar/lnpdqp](https://jsr.io/wildboar/lnpdqp) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
