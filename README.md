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

## Latest list — 2026-11-17 10:19 UTC

New modules created between 2026-11-17 09:19 UTC and 2026-11-17 10:19 UTC.

[Full CSV](data/new-deno-modules-2026-11-17T10-19-02-987697Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-17 09:31:02 | [komga-plugin-bridge/plugin-api](https://jsr.io/komga-plugin-bridge/plugin-api) | 0.1.0 | 70 | Types for writing Komga plugins: hooks, settings, storage and Komga data access… |
| 2026-11-17 09:37:41 | [komga-plugin-bridge/test-runner](https://jsr.io/komga-plugin-bridge/test-runner) | 0.1.1 | 47 | Runs a Komga plugin against stand-ins for Komga, with no Komga needed. Not affi… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
