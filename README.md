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

## Latest list — 2026-10-14 23:21 UTC

New modules created between 2026-10-14 22:19 UTC and 2026-10-14 23:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-14T23-21-30-81058Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-14 22:20:24 | [mirrordown/sat-slug](https://jsr.io/mirrordown/sat-slug) |  |  | A Sätteri plugin that adds GitHub-style id slugs to headings. |
| 2026-10-14 22:20:31 | [mirrordown/sat-github-alerts](https://jsr.io/mirrordown/sat-github-alerts) |  |  | A Sätteri plugin for GitHub-style alerts (> [!NOTE], > [!WARNING], …). |
| 2026-10-14 22:20:40 | [mirrordown/sat-mark](https://jsr.io/mirrordown/sat-mark) |  |  | A Sätteri plugin for highlight syntax (==text==), rendering <mark> elements. |
| 2026-10-14 22:20:59 | [mirrordown/preset-satteri](https://jsr.io/mirrordown/preset-satteri) |  |  | The Mirrordown suite for Sätteri in one call. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
