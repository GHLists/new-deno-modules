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

## Latest list — 2026-10-23 06:22 UTC

New modules created between 2026-10-23 05:21 UTC and 2026-10-23 06:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-23T06-22-04-669912Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-23 05:50:12 | [cosys/crypto](https://jsr.io/cosys/crypto) | 0.1.1 | 70 |  |
| 2026-10-23 05:50:22 | [cosys/record](https://jsr.io/cosys/record) | 0.1.1 | 64 |  |
| 2026-10-23 05:50:32 | [cosys/peer](https://jsr.io/cosys/peer) | 0.1.1 | 76 |  |
| 2026-10-23 05:50:41 | [cosys/posts](https://jsr.io/cosys/posts) | 0.1.1 | 64 |  |
| 2026-10-23 05:51:11 | [cosys/bridge](https://jsr.io/cosys/bridge) | 0.1.1 | 64 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
