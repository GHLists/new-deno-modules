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

## Latest list — 2026-10-17 07:20 UTC

New modules created between 2026-10-17 06:20 UTC and 2026-10-17 07:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-17T07-20-24-056599Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-17 06:27:55 | [ende/net](https://jsr.io/ende/net) | 2026.10.15 | 88 | Utilities for working with the network |
| 2026-10-17 06:44:11 | [ende/http](https://jsr.io/ende/http) | 2026.10.15 | 88 | Utilities for building HTTP servers |
| 2026-10-17 06:46:51 | [ende/ini](https://jsr.io/ende/ini) | 2026.10.15 | 94 | Parsing and serializing of INI files |
| 2026-10-17 06:48:07 | [ende/io](https://jsr.io/ende/io) | 2026.10.15 | 94 | The utilities for advanced I/O operations using Reader and Writer interfaces. |
| 2026-10-17 06:49:31 | [ende/json](https://jsr.io/ende/json) | 2026.10.15 | 94 | (Streaming) parsing and serializing of JSON files |
| 2026-10-17 06:50:57 | [ende/jsonc](https://jsr.io/ende/jsonc) | 2026.10.15 | 94 | Parsing and serializing of JSONC files |
| 2026-10-17 06:52:12 | [ende/math](https://jsr.io/ende/math) | 2026.10.15 | 94 | Basic math utilities |
| 2026-10-17 06:53:54 | [ende/msgpack](https://jsr.io/ende/msgpack) | 2026.10.15 | 94 | Encoding and decoding for the msgpack format |
| 2026-10-17 06:55:11 | [ende/random](https://jsr.io/ende/random) | 2026.10.15 | 94 | Various utilities using random number generators. The package also provides see… |
| 2026-10-17 06:56:24 | [ende/regexp](https://jsr.io/ende/regexp) | 2026.10.15 | 94 | Utilities for working with RegExp |
| 2026-10-17 06:57:33 | [ende/semver](https://jsr.io/ende/semver) | 2026.10.15 | 94 | Parsing and comparing of semantic versions (SemVer) |
| 2026-10-17 06:58:53 | [ende/tar](https://jsr.io/ende/tar) | 2026.10.15 | 94 | Streaming utilities for working with tar archives. |
| 2026-10-17 07:00:18 | [ende/testing](https://jsr.io/ende/testing) | 2026.10.15 | 88 | Tools for testing Deno code like snapshot testing, bdd testing, and time mockin… |
| 2026-10-17 07:02:43 | [ende/text](https://jsr.io/ende/text) | 2026.10.15 | 94 | Utilities for working with text |
| 2026-10-17 07:03:53 | [ende/ulid](https://jsr.io/ende/ulid) | 2026.10.15 | 94 | Generation of Universally Unique Lexicographically Sortable Identifiers (ULIDs) |
| 2026-10-17 07:05:12 | [ende/uuid](https://jsr.io/ende/uuid) | 2026.10.15 | 94 | Generators and validators for UUIDs |
| 2026-10-17 07:06:35 | [ende/webgpu](https://jsr.io/ende/webgpu) | 2026.10.15 | 88 |  |
| 2026-10-17 07:07:47 | [ende/xml](https://jsr.io/ende/xml) | 2026.10.15 | 100 | XML parsing and serialization |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
