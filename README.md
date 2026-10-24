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

## Latest list — 2026-10-24 19:20 UTC

New modules created between 2026-10-24 18:19 UTC and 2026-10-24 19:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-24T19-20-12-306337Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-24 18:59:36 | [panth977/icebase](https://jsr.io/panth977/icebase) | 0.1.1 | 70 | Firebase's client API with an explicit schema, declared indexes and modes per s… |
| 2026-10-24 18:59:40 | [panth977/icebase-server](https://jsr.io/panth977/icebase-server) | 0.1.1 | 70 | IceBase on the server: admin, typed functions/v2 triggers, and the custom-auth… |
| 2026-10-24 18:59:42 | [panth977/icebase-cli](https://jsr.io/panth977/icebase-cli) | 0.1.1 | 64 | The icebase CLI (init, dev, deploy, indexes check), management APIs and the Ice… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
