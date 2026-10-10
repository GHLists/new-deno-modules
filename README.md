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

## Latest list — 2026-10-10 11:19 UTC

New modules created between 2026-10-10 10:18 UTC and 2026-10-10 11:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-10T11-19-24-628215Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-10 10:48:28 | [mikepage/flareosaur](https://jsr.io/mikepage/flareosaur) | 20261010.0.2 | 100 | The Deno standard library, ported to run on Cloudflare Workers without nodejs_c… |
| 2026-10-10 11:05:15 | [wildboar/lpp](https://jsr.io/wildboar/lpp) |  |  |  |
| 2026-10-10 11:09:46 | [realdigit/oauth-server](https://jsr.io/realdigit/oauth-server) | 0.1.0 | 64 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
