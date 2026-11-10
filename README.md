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

## Latest list — 2026-11-10 20:22 UTC

New modules created between 2026-11-10 19:19 UTC and 2026-11-10 20:22 UTC.

[Full CSV](data/new-deno-modules-2026-11-10T20-22-20-008626Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-10 20:04:43 | [tekservix/smsgora](https://jsr.io/tekservix/smsgora) | 1.0.0 | 100 | SMS Gora SMS gateway client: send and receive SMS through your own Android phon… |
| 2026-11-10 20:06:41 | [tekservix/waservix](https://jsr.io/tekservix/waservix) | 1.0.0 | 100 | WAservix WhatsApp API gateway client: send WhatsApp text, media, locations and… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
