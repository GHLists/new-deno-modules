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

## Latest list — 2026-10-28 23:19 UTC

New modules created between 2026-10-28 22:20 UTC and 2026-10-28 23:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-28T23-19-11-54294Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-28 23:08:40 | [mirrordown/mdit-tab-icons](https://jsr.io/mirrordown/mdit-tab-icons) |  |  | A markdown-it plugin to add icons to tab labels: matched from the label, or nam… |
| 2026-10-28 23:09:03 | [mirrordown/remd-tab-icons](https://jsr.io/mirrordown/remd-tab-icons) |  |  | A rehype plugin to add icons to tab labels: matched from the label, or named wi… |
| 2026-10-28 23:09:15 | [mirrordown/sat-tab-icons](https://jsr.io/mirrordown/sat-tab-icons) |  |  | A Sätteri plugin to add icons to tab labels: matched from the label, or named w… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
