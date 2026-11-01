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

## Latest list — 2026-11-01 21:20 UTC

New modules created between 2026-11-01 20:20 UTC and 2026-11-01 21:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-01T21-20-42-90137Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-01 20:24:14 | [node-jhora/analytics](https://jsr.io/node-jhora/analytics) |  |  | Shadbala, Ashtakavarga, yoga detection and KP significators for the node-jhora… |
| 2026-11-01 20:24:16 | [node-jhora/api](https://jsr.io/node-jhora/api) |  |  | Fastify REST API server exposing the node-jhora Vedic astrology engine as JSON… |
| 2026-11-01 20:24:19 | [node-jhora/atlas](https://jsr.io/node-jhora/atlas) |  |  | Offline GeoNames city gazetteer with multilingual prefix search and browser-saf… |
| 2026-11-01 20:24:20 | [node-jhora/engine](https://jsr.io/node-jhora/engine) |  |  | Lazy, memoised ChartSession facade over node-jhora core, analytics and predicti… |
| 2026-11-01 20:24:22 | [node-jhora/events](https://jsr.io/node-jhora/events) |  |  | Exact sign ingresses, stations and custom astronomical events for the node-jhor… |
| 2026-11-01 20:24:23 | [node-jhora/format](https://jsr.io/node-jhora/format) |  |  | Versioned .njh chart file format for node-jhora: Zod validation, JSON Schema, m… |
| 2026-11-01 20:24:25 | [node-jhora/match](https://jsr.io/node-jhora/match) |  |  | Vedic marriage compatibility: Ashta Kuta (36 points), Dasha Kuta (10 Poruthams)… |
| 2026-11-01 20:24:27 | [node-jhora/prediction](https://jsr.io/node-jhora/prediction) |  |  | Vimshottari, Yogini, Narayana and Chara dashas, transit scanning and Jaimini to… |
| 2026-11-01 20:24:28 | [node-jhora/reporting](https://jsr.io/node-jhora/reporting) |  |  | PDF birth chart reports (positions, houses, Shadbala, yogas, chart diagrams) fo… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
