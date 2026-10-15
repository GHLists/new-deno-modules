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

## Latest list — 2026-10-15 03:20 UTC

New modules created between 2026-10-15 02:21 UTC and 2026-10-15 03:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-15T03-20-06-009219Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-15 02:22:21 | [ende/cache](https://jsr.io/ende/cache) | 2026.10.14 | 88 | UNSTABLE: Cache utilities |
| 2026-10-15 02:30:27 | [ende/streams](https://jsr.io/ende/streams) | 2026.10.14 | 88 | Utilities for working with the Web Streams API |
| 2026-10-15 02:38:53 | [ende/cbor](https://jsr.io/ende/cbor) | 2026.10.14 | 88 | UNSTABLE: Utilities for parsing and serializing Concise Binary Object Represent… |
| 2026-10-15 02:46:19 | [ende/fmt](https://jsr.io/ende/fmt) | 2026.10.14 | 94 | Utilities for formatting values, such as adding colors to text, formatting dura… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
