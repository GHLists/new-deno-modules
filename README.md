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

## Latest list — 2026-10-10 14:18 UTC

New modules created between 2026-10-10 13:18 UTC and 2026-10-10 14:18 UTC.

[Full CSV](data/new-deno-modules-2026-10-10T14-18-51-005045Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-10 13:19:18 | [steno/plugin-markdown-extensions](https://jsr.io/steno/plugin-markdown-extensions) | 0.1.1 | 82 |  |
| 2026-10-10 13:20:25 | [steno/plugin-nav](https://jsr.io/steno/plugin-nav) | 0.1.1 | 82 |  |
| 2026-10-10 13:21:12 | [steno/plugin-backlinks](https://jsr.io/steno/plugin-backlinks) | 0.1.1 | 82 |  |
| 2026-10-10 13:21:54 | [steno/plugin-accent-color](https://jsr.io/steno/plugin-accent-color) | 0.1.1 | 82 |  |
| 2026-10-10 13:22:36 | [steno/plugin-directives](https://jsr.io/steno/plugin-directives) | 0.1.1 | 82 |  |
| 2026-10-10 13:23:10 | [steno/plugin-taxonomy](https://jsr.io/steno/plugin-taxonomy) | 0.1.1 | 82 |  |
| 2026-10-10 13:24:12 | [steno/plugin-csp](https://jsr.io/steno/plugin-csp) | 0.1.1 | 82 |  |
| 2026-10-10 14:03:58 | [vanaware/mdblog](https://jsr.io/vanaware/mdblog) |  |  | Browser Blog engine from markdown |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
