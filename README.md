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

## Latest list — 2026-11-18 19:21 UTC

New modules created between 2026-11-18 18:21 UTC and 2026-11-18 19:21 UTC.

[Full CSV](data/new-deno-modules-2026-11-18T19-21-02-365863Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-18 18:27:10 | [sekhmet/schema](https://jsr.io/sekhmet/schema) | 0.1.0 | 94 |  |
| 2026-11-18 18:39:16 | [dibs/dibs](https://jsr.io/dibs/dibs) | 0.1.2 | 82 |  |
| 2026-11-18 18:44:32 | [dibs/pi](https://jsr.io/dibs/pi) |  |  |  |
| 2026-11-18 18:45:45 | [dibs/opencode](https://jsr.io/dibs/opencode) |  |  |  |
| 2026-11-18 18:55:53 | [edwindragusin/sistema-diseno](https://jsr.io/edwindragusin/sistema-diseno) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
