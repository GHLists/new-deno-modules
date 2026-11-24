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

## Latest list — 2026-11-24 17:22 UTC

New modules created between 2026-11-24 16:19 UTC and 2026-11-24 17:22 UTC.

[Full CSV](data/new-deno-modules-2026-11-24T17-22-10-906056Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-24 16:33:58 | [sunasty/har-sanitizer](https://jsr.io/sunasty/har-sanitizer) | 1.0.0 | 52 |  |
| 2026-11-24 16:34:02 | [sunasty/tournament-math](https://jsr.io/sunasty/tournament-math) | 1.0.0 | 52 |  |
| 2026-11-24 16:34:05 | [sunasty/code128-svg](https://jsr.io/sunasty/code128-svg) | 1.0.0 | 52 |  |
| 2026-11-24 16:35:04 | [sunasty/color-math](https://jsr.io/sunasty/color-math) | 1.0.0 | 52 |  |
| 2026-11-24 16:35:07 | [sunasty/qr-payload](https://jsr.io/sunasty/qr-payload) | 1.0.0 | 52 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
