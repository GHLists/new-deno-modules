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

## Latest list — 2026-11-05 10:20 UTC

New modules created between 2026-11-05 09:20 UTC and 2026-11-05 10:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-05T10-20-28-91293Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-05 10:02:13 | [swarmfu/connect-protocol](https://jsr.io/swarmfu/connect-protocol) | 0.1.1 | 58 |  |
| 2026-11-05 10:02:16 | [corsin/core](https://jsr.io/corsin/core) |  |  |  |
| 2026-11-05 10:11:03 | [postext/postext](https://jsr.io/postext/postext) |  |  |  |
| 2026-11-05 10:13:39 | [postext/bundle](https://jsr.io/postext/bundle) |  |  |  |
| 2026-11-05 10:14:33 | [postext/pdf](https://jsr.io/postext/pdf) |  |  |  |
| 2026-11-05 10:15:04 | [postext/epub](https://jsr.io/postext/epub) |  |  |  |
| 2026-11-05 10:15:39 | [postext/citeproc](https://jsr.io/postext/citeproc) |  |  |  |
| 2026-11-05 10:16:05 | [postext/scorm](https://jsr.io/postext/scorm) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
