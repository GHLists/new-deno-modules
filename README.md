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

## Latest list — 2026-10-07 14:22 UTC

New modules created between 2026-10-07 13:22 UTC and 2026-10-07 14:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-07T14-22-36-034055Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-07 13:38:42 | [wildboar/smrse](https://jsr.io/wildboar/smrse) |  |  |  |
| 2026-10-07 13:42:57 | [wildboar/spnego](https://jsr.io/wildboar/spnego) | 1.0.0 | 100 | SPNEGO ASN.1 data structures and functions for encoding and decoding them. |
| 2026-10-07 13:53:59 | [sewlore/sewing-math](https://jsr.io/sewlore/sewing-math) | 0.1.0 | 82 | Pure sewing measurement helpers: unit conversion, fabric stretch and recovery,… |
| 2026-10-07 14:13:10 | [lavender/jsonv2](https://jsr.io/lavender/jsonv2) | 1.0.1 | 70 | lightweight JSON file library for config files,data etc.. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
