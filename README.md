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

## Latest list — 2026-10-18 04:18 UTC

New modules created between 2026-10-18 03:19 UTC and 2026-10-18 04:18 UTC.

[Full CSV](data/new-deno-modules-2026-10-18T04-18-43-952143Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-18 03:29:34 | [gukhanmun/loanwords-cdb](https://jsr.io/gukhanmun/loanwords-cdb) |  |  | NIKL loanword examples bundled as a CDB binary for @gukhanmun/wasm and @gukhanm… |
| 2026-10-18 03:30:27 | [gukhanmun/loanwords-fst](https://jsr.io/gukhanmun/loanwords-fst) |  |  | NIKL loanword examples bundled as an FST binary for @gukhanmun/wasm and @gukhan… |
| 2026-10-18 04:05:57 | [nuten/format](https://jsr.io/nuten/format) |  |  | A formatter for Nushell. Robust, fast, and lightweight. |
| 2026-10-18 04:06:11 | [nuten/prettier-plugin](https://jsr.io/nuten/prettier-plugin) |  |  | The Prettier plugin of Nuten, a formatter for Nushell. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
