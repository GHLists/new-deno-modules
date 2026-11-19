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

## Latest list — 2026-11-19 19:19 UTC

New modules created between 2026-11-19 18:22 UTC and 2026-11-19 19:19 UTC.

[Full CSV](data/new-deno-modules-2026-11-19T19-19-07-695729Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-19 18:34:03 | [wyattjoh/dexcom](https://jsr.io/wyattjoh/dexcom) | 0.1.0 | 88 |  |
| 2026-11-19 18:34:12 | [wyattjoh/dexcom-mcp](https://jsr.io/wyattjoh/dexcom-mcp) | 0.1.0 | 88 |  |
| 2026-11-19 18:50:50 | [zuccadev-labs/zenith](https://jsr.io/zuccadev-labs/zenith) | 0.1.0 | 70 |  |
| 2026-11-19 18:51:22 | [zuccadev-labs/zenith-cli](https://jsr.io/zuccadev-labs/zenith-cli) | 0.2.0 | 70 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
