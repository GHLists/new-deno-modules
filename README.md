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

## Latest list — 2026-10-15 04:22 UTC

New modules created between 2026-10-15 03:20 UTC and 2026-10-15 04:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-15T04-22-04-151965Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-15 03:26:00 | [ende/collections](https://jsr.io/ende/collections) | 2026.10.14 | 88 | Pure functions for common tasks related to collection types like arrays and obj… |
| 2026-10-15 03:28:16 | [ende/crypto](https://jsr.io/ende/crypto) | 2026.10.14 | 88 | Extensions to the Web Crypto API |
| 2026-10-15 03:31:49 | [ende/csv](https://jsr.io/ende/csv) | 2026.10.14 | 88 | Reading and writing of comma-separated values (CSV) files. |
| 2026-10-15 03:34:11 | [ende/datetime](https://jsr.io/ende/datetime) | 2026.10.14 | 88 | Utilities for dealing with Date objects. |
| 2026-10-15 03:39:08 | [ende/dotenv](https://jsr.io/ende/dotenv) | 2026.10.14 | 88 | Parsing and loading environment variables from an `.env` file. |
| 2026-10-15 03:44:36 | [ende/encoding](https://jsr.io/ende/encoding) | 2026.10.14 | 94 | Utilities for encoding and decoding common formats like hex, base64, and varint. |
| 2026-10-15 03:51:59 | [ende/path](https://jsr.io/ende/path) | 2026.10.14 | 88 | Utilities for working with file system paths. |
| 2026-10-15 04:02:06 | [ende/expect](https://jsr.io/ende/expect) | 2026.10.14 | 88 | Jest compatible `expect` assertion functions |
| 2026-10-15 04:05:58 | [ende/cli](https://jsr.io/ende/cli) | 2026.10.14 | 88 | Tools for creating interactive command line tools. |
| 2026-10-15 04:10:08 | [ende/toml](https://jsr.io/ende/toml) | 2026.10.14 | 88 | Parsing and serializing of TOML files. |
| 2026-10-15 04:13:25 | [ende/yaml](https://jsr.io/ende/yaml) | 2026.10.14 | 88 | Parsing and serializing of YAML files. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
