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

## Latest list — 2026-10-26 01:21 UTC

New modules created between 2026-10-26 00:20 UTC and 2026-10-26 01:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-26T01-21-37-760885Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-26 00:54:59 | [saxby/cli](https://jsr.io/saxby/cli) |  |  |  |
| 2026-10-26 00:57:35 | [saxby/core](https://jsr.io/saxby/core) |  |  |  |
| 2026-10-26 00:58:07 | [saxby/llm-router](https://jsr.io/saxby/llm-router) |  |  |  |
| 2026-10-26 00:58:53 | [saxby/vram-guard-mac](https://jsr.io/saxby/vram-guard-mac) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
