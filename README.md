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

## Latest list — 2026-10-28 16:19 UTC

New modules created between 2026-10-28 15:19 UTC and 2026-10-28 16:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-28T16-19-01-774223Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-28 15:36:41 | [mirrordown/mdit-caption](https://jsr.io/mirrordown/mdit-caption) |  |  | A markdown-it plugin to caption any block with a ~: line after it, wrapping it… |
| 2026-10-28 15:36:46 | [mirrordown/remd-caption](https://jsr.io/mirrordown/remd-caption) |  |  | A remark plugin to caption any block with a ~: line after it, wrapping it in <f… |
| 2026-10-28 15:36:51 | [mirrordown/sat-caption](https://jsr.io/mirrordown/sat-caption) |  |  | A Sätteri plugin to caption any block with a ~: line after it, wrapping it in <… |
| 2026-10-28 16:12:03 | [nuin/msa-canvas](https://jsr.io/nuin/msa-canvas) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
