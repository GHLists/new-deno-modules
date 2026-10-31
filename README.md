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

## Latest list — 2026-10-31 04:19 UTC

New modules created between 2026-10-31 03:18 UTC and 2026-10-31 04:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-31T04-19-29-983611Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-31 03:48:19 | [glowcap/abi](https://jsr.io/glowcap/abi) |  |  |  |
| 2026-10-31 03:49:29 | [glowcap/runtime](https://jsr.io/glowcap/runtime) |  |  |  |
| 2026-10-31 03:49:57 | [glowcap/tcp](https://jsr.io/glowcap/tcp) |  |  |  |
| 2026-10-31 03:50:24 | [glowcap/iroh](https://jsr.io/glowcap/iroh) |  |  |  |
| 2026-10-31 03:50:50 | [glowcap/inproc](https://jsr.io/glowcap/inproc) |  |  |  |
| 2026-10-31 03:51:28 | [glowcap/onion](https://jsr.io/glowcap/onion) |  |  |  |
| 2026-10-31 03:51:53 | [glowcap/web](https://jsr.io/glowcap/web) |  |  |  |
| 2026-10-31 03:52:14 | [glowcap/webrtc](https://jsr.io/glowcap/webrtc) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
