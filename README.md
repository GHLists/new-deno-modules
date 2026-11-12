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

## Latest list — 2026-11-12 18:20 UTC

New modules created between 2026-11-12 17:20 UTC and 2026-11-12 18:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-12T18-20-59-77137Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-12 17:51:37 | [tundraconnect/open-meteo](https://jsr.io/tundraconnect/open-meteo) | 0.1.0 | 100 | Typed Open-Meteo client: Forecast, Ensemble (every member), Previous Runs, Hist… |
| 2026-11-12 17:52:34 | [tundraconnect/aviationweather](https://jsr.io/tundraconnect/aviationweather) | 0.1.0 | 100 | Typed aviationweather.gov client: METAR/SPECI observations, TAFs and the bulk M… |
| 2026-11-12 17:52:39 | [tundraconnect/eia](https://jsr.io/tundraconnect/eia) | 0.1.0 | 100 | Typed U.S. EIA Open Data API v2 client: any route and facet, auto-pagination pa… |
| 2026-11-12 17:52:41 | [tundraconnect/deribit](https://jsr.io/tundraconnect/deribit) | 0.1.0 | 100 | Typed Deribit client: option chains, book summaries and historical trades over… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
