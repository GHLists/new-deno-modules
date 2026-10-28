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

## Latest list — 2026-10-28 08:21 UTC

New modules created between 2026-10-28 07:18 UTC and 2026-10-28 08:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-28T08-21-17-488067Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-28 07:39:19 | [mirrordown/mdit-mermaid-pele](https://jsr.io/mirrordown/mdit-mermaid-pele) |  |  | A markdown-it plugin to render mermaid code blocks to inline SVG with Pele, the… |
| 2026-10-28 07:40:28 | [mirrordown/remd-mermaid-pele](https://jsr.io/mirrordown/remd-mermaid-pele) |  |  | A rehype plugin to render mermaid code blocks to inline SVG with Pele, themed w… |
| 2026-10-28 07:41:19 | [mirrordown/sat-mermaid-pele](https://jsr.io/mirrordown/sat-mermaid-pele) |  |  | A Sätteri plugin to render mermaid code blocks to inline SVG with Pele, themed… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
