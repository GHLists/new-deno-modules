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

## Latest list — 2026-10-16 01:20 UTC

New modules created between 2026-10-16 00:19 UTC and 2026-10-16 01:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-16T01-20-25-703215Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-16 00:53:27 | [noflo/assembly-utils](https://jsr.io/noflo/assembly-utils) |  |  |  |
| 2026-10-16 00:53:51 | [noflo/fbp-client](https://jsr.io/noflo/fbp-client) |  |  |  |
| 2026-10-16 00:54:29 | [noflo/runtime-client](https://jsr.io/noflo/runtime-client) |  |  |  |
| 2026-10-16 00:56:29 | [s0fractal/warrant](https://jsr.io/s0fractal/warrant) | 0.10.0 | 82 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
