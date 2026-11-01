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

## Latest list — 2026-11-01 00:20 UTC

New modules created between 2026-10-31 23:20 UTC and 2026-11-01 00:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-01T00-20-29-854894Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-01 00:09:25 | [baxyz/mozlz4](https://jsr.io/baxyz/mozlz4) |  |  | Encode and decode Mozilla's mozLz40 format (LZ4 variant used by Firefox and Zen… |
| 2026-11-01 00:09:40 | [baxyz/sqlite-reader](https://jsr.io/baxyz/sqlite-reader) |  |  | Read-only SQLite3 binary parser: extract rows from a table given a raw file buf… |
| 2026-11-01 00:13:43 | [arbyachat/arbya-chat](https://jsr.io/arbyachat/arbya-chat) |  |  | Official TypeScript & JavaScript SDK for Arbya Chat (عربية شات - https://arbya.… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
