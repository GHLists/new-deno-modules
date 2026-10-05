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

## Latest list — 2026-10-05 07:22 UTC

New modules created between 2026-10-05 06:20 UTC and 2026-10-05 07:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-05T07-22-38-154951Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-05 07:04:39 | [dui/util](https://jsr.io/dui/util) | 0.7.2 | 88 | AiCube2028 通用工具套件：加解密、JWT、ConfigStore、Logger、InnerAPI、gwFetch。 |
| 2026-10-05 07:16:53 | [philc/lint-rules](https://jsr.io/philc/lint-rules) | 0.1.0 | 82 |  |
| 2026-10-05 07:17:24 | [dui/translate-google](https://jsr.io/dui/translate-google) | 0.1.0 | 47 |  |
| 2026-10-05 07:18:06 | [dui/mcp](https://jsr.io/dui/mcp) |  |  |  |
| 2026-10-05 07:21:50 | [dui/storage](https://jsr.io/dui/storage) | 0.2.0 | 58 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
