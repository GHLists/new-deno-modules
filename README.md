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

## Latest list — 2026-09-27 13:21 UTC

New modules created between 2026-09-27 12:20 UTC and 2026-09-27 13:21 UTC.

[Full CSV](data/new-deno-modules-2026-09-27T13-21-53-272021Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-09-27 12:36:59 | [sileanhell/vite-plugin-tailwind-mangle](https://jsr.io/sileanhell/vite-plugin-tailwind-mangle) | 0.1.0 | 64 |  |
| 2026-09-27 12:52:35 | [dw24/gsign](https://jsr.io/dw24/gsign) | 0.1.0 | 76 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
