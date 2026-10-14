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

## Latest list — 2026-10-14 22:19 UTC

New modules created between 2026-10-14 21:20 UTC and 2026-10-14 22:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-14T22-19-16-046342Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-14 21:37:45 | [tlockney/cdp-kernel](https://jsr.io/tlockney/cdp-kernel) | 0.1.1 | 76 | A Jupyter kernel extracted from Deno's (deno jupyter, v2.9.6) that drives any V… |
| 2026-10-14 21:40:39 | [mirrordown/preset-markdown-it](https://jsr.io/mirrordown/preset-markdown-it) |  |  | The full Mirrordown suite for markdown-it in one plugin. |
| 2026-10-14 21:40:51 | [mirrordown/preset-remark](https://jsr.io/mirrordown/preset-remark) |  |  | The full Mirrordown suite for remark/rehype (unified) in one call. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
