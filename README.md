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

## Latest list — 2026-09-29 17:23 UTC

New modules created between 2026-09-29 16:20 UTC and 2026-09-29 17:23 UTC.

[Full CSV](data/new-deno-modules-2026-09-29T17-23-34-606167Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-09-29 16:40:22 | [nodef/extra-lists](https://jsr.io/nodef/extra-lists) | 4.2.0 | 100 | A collection of functions for operating upon Lists. |
| 2026-09-29 17:03:46 | [wxn0brp/db](https://jsr.io/wxn0brp/db) | 0.120.2 | 76 | A modular, embedded database for developers who want control over their data st… |
| 2026-09-29 17:05:38 | [nodef/extra-wordnet](https://jsr.io/nodef/extra-wordnet) |  |  | WordNet is a lexical database of semantic relations between words. |
| 2026-09-29 17:13:06 | [gamerelay/sdk](https://jsr.io/gamerelay/sdk) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
