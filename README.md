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

## Latest list — 2026-10-25 06:22 UTC

New modules created between 2026-10-25 05:19 UTC and 2026-10-25 06:22 UTC.

[Full CSV](data/new-deno-modules-2026-10-25T06-22-14-538252Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-25 06:10:53 | [bearmetal/devtools](https://jsr.io/bearmetal/devtools) | 0.0.1 | 47 |  |
| 2026-10-25 06:18:33 | [truckleap/reefer-burn](https://jsr.io/truckleap/reefer-burn) |  |  | Reefer unit fuel burn and cost estimates for a trip |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
