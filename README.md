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

## Latest list — 2026-10-27 06:20 UTC

New modules created between 2026-10-27 05:20 UTC and 2026-10-27 06:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-27T06-20-03-712475Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-27 05:38:14 | [blazediff/codec-png-native](https://jsr.io/blazediff/codec-png-native) | 6.1.0 | 82 |  |
| 2026-10-27 05:38:24 | [blazediff/codec-png-wasm](https://jsr.io/blazediff/codec-png-wasm) | 6.1.0 | 82 |  |
| 2026-10-27 05:43:08 | [bctl/libprotocol](https://jsr.io/bctl/libprotocol) | 0.1.0 | 35 |  |
| 2026-10-27 05:43:20 | [bctl/libexperiment](https://jsr.io/bctl/libexperiment) | 0.1.1 | 52 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
