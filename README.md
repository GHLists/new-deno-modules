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

## Latest list — 2026-10-04 18:20 UTC

New modules created between 2026-10-04 17:21 UTC and 2026-10-04 18:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-04T18-20-04-031579Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-04 17:28:58 | [tundraconnect/cloudflare-dns](https://jsr.io/tundraconnect/cloudflare-dns) | 0.1.0 | 100 | Typed Cloudflare DNS client: list, create, update and delete DNS records, apply… |
| 2026-10-04 17:28:59 | [tundraconnect/cloudflare-saas](https://jsr.io/tundraconnect/cloudflare-saas) | 0.1.0 | 100 | Typed Cloudflare for SaaS client: add and manage customer custom hostnames, tra… |
| 2026-10-04 17:29:47 | [tundraconnect/google-analytics](https://jsr.io/tundraconnect/google-analytics) | 0.1.0 | 100 | Typed GA4 Measurement Protocol client: send server-side events and validate the… |
| 2026-10-04 17:29:48 | [tundraconnect/cloudflare-turnstile](https://jsr.io/tundraconnect/cloudflare-turnstile) | 0.1.0 | 100 | Typed Cloudflare Turnstile client: verify widget tokens server-side, check the… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
