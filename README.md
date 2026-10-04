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

## Latest list — 2026-10-04 16:22 UTC

New modules created between 2026-10-04 15:21 UTC and 2026-10-04 16:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-04T16-22-04-070363Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-04 15:21:29 | [wormblossom/macromania-webtt](https://jsr.io/wormblossom/macromania-webtt) | 0.1.0 | 58 |  |
| 2026-10-04 15:44:56 | [viviengraffin/translation-vue](https://jsr.io/viviengraffin/translation-vue) | 2.0.1 | 52 |  |
| 2026-10-04 15:45:09 | [dssutg/dss-ui-kit](https://jsr.io/dssutg/dss-ui-kit) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
