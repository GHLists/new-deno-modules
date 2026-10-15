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

## Latest list — 2026-10-15 00:21 UTC

New modules created between 2026-10-14 23:21 UTC and 2026-10-15 00:21 UTC.

[Full CSV](data/new-deno-modules-2026-10-15T00-21-52-914368Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-14 23:52:36 | [mirrordown/sat-del](https://jsr.io/mirrordown/sat-del) |  |  | A Sätteri plugin for deletion syntax (--text--), rendering <del> elements. |
| 2026-10-14 23:52:44 | [mirrordown/sat-ins](https://jsr.io/mirrordown/sat-ins) |  |  | A Sätteri plugin for insertion syntax (++text++), rendering <ins> elements. |
| 2026-10-14 23:52:52 | [mirrordown/sat-kbd](https://jsr.io/mirrordown/sat-kbd) |  |  | A Sätteri plugin for keyboard-key syntax ([[Ctrl]]), rendering <kbd> elements. |
| 2026-10-14 23:53:01 | [mirrordown/sat-spoiler](https://jsr.io/mirrordown/sat-spoiler) |  |  | A Sätteri plugin for Discord-style spoiler syntax (\|\|text\|\|), rendering JavaScr… |
| 2026-10-15 00:14:14 | [mirrordown/sat-squeeze-paragraphs](https://jsr.io/mirrordown/sat-squeeze-paragraphs) |  |  | A Sätteri plugin that removes empty (whitespace-only) paragraphs. |
| 2026-10-15 00:14:22 | [mirrordown/sat-unwrap-images](https://jsr.io/mirrordown/sat-unwrap-images) |  |  | A Sätteri plugin that unwraps images out of paragraphs that hold nothing else. |
| 2026-10-15 00:14:29 | [mirrordown/sat-sectionize](https://jsr.io/mirrordown/sat-sectionize) |  |  | A Sätteri plugin that wraps headings and their content in <section> elements. |
| 2026-10-15 00:14:39 | [mirrordown/sat-lightbox](https://jsr.io/mirrordown/sat-lightbox) |  |  | A Sätteri plugin that opts images into a JavaScript-free <dialog> lightbox with… |
| 2026-10-15 00:15:00 | [mirrordown/sat-autolink-headings](https://jsr.io/mirrordown/sat-autolink-headings) |  |  | A Sätteri plugin that adds self-referential anchor links to headings with an id. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
