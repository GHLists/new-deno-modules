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

## Latest list — 2026-11-11 01:19 UTC

New modules created between 2026-11-11 00:22 UTC and 2026-11-11 01:19 UTC.

[Full CSV](data/new-deno-modules-2026-11-11T01-19-28-585476Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-11 01:01:44 | [pulsify/lexical](https://jsr.io/pulsify/lexical) |  |  |  |
| 2026-11-11 01:01:49 | [pulsify/tauri](https://jsr.io/pulsify/tauri) | 6.0.0 | 70 |  |
| 2026-11-11 01:09:05 | [pulsify/react](https://jsr.io/pulsify/react) | 6.0.0 | 82 |  |
| 2026-11-11 01:09:56 | [pulsify/cloud](https://jsr.io/pulsify/cloud) | 6.0.0 | 64 |  |
| 2026-11-11 01:11:00 | [pulsify/cloud-server](https://jsr.io/pulsify/cloud-server) |  |  |  |
| 2026-11-11 01:12:03 | [pulsify/indexeddb](https://jsr.io/pulsify/indexeddb) | 6.0.0 | 70 |  |
| 2026-11-11 01:12:06 | [pulsify/prosemirror](https://jsr.io/pulsify/prosemirror) |  |  |  |
| 2026-11-11 01:12:09 | [pulsify/electron](https://jsr.io/pulsify/electron) | 6.0.0 | 70 |  |
| 2026-11-11 01:12:12 | [pulsify/core](https://jsr.io/pulsify/core) | 6.0.0 | 52 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
