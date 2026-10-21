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

## Latest list — 2026-10-21 12:20 UTC

New modules created between 2026-10-21 11:22 UTC and 2026-10-21 12:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-21T12-20-47-006195Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-21 12:03:24 | [graphql-markdown/core](https://jsr.io/graphql-markdown/core) |  |  | Core of GraphQL-Markdown: generates Markdown documentation from a GraphQL schem… |
| 2026-10-21 12:04:14 | [graphql-markdown/types](https://jsr.io/graphql-markdown/types) |  |  |  |
| 2026-10-21 12:04:34 | [graphql-markdown/telemetry](https://jsr.io/graphql-markdown/telemetry) |  |  | Anonymous, opt-out usage telemetry for the GraphQL-Markdown CLI. |
| 2026-10-21 12:04:52 | [graphql-markdown/printer-legacy](https://jsr.io/graphql-markdown/printer-legacy) |  |  | Default Markdown/MDX printer for GraphQL-Markdown, rendering GraphQL schema typ… |
| 2026-10-21 12:05:10 | [graphql-markdown/diff](https://jsr.io/graphql-markdown/diff) |  |  | Detects GraphQL schema changes so GraphQL-Markdown only regenerates documentati… |
| 2026-10-21 12:05:25 | [graphql-markdown/helpers](https://jsr.io/graphql-markdown/helpers) |  |  | Helpers for customizing GraphQL-Markdown output, such as directives and custom… |
| 2026-10-21 12:05:39 | [graphql-markdown/graphql](https://jsr.io/graphql-markdown/graphql) |  |  | GraphQL schema loading, introspection and type utilities for GraphQL-Markdown. |
| 2026-10-21 12:05:54 | [graphql-markdown/formatters](https://jsr.io/graphql-markdown/formatters) |  |  | Formatter presets for GraphQL-Markdown: Docusaurus, Starlight, Fumadocs, Vocs,… |
| 2026-10-21 12:06:25 | [graphql-markdown/logger](https://jsr.io/graphql-markdown/logger) |  |  | Logger used by the GraphQL-Markdown packages. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
