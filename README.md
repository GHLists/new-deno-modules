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

## Latest list — 2026-10-08 06:20 UTC

New modules created between 2026-10-08 05:18 UTC and 2026-10-08 06:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-08T06-20-51-212552Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-08 06:05:08 | [noflo/graph](https://jsr.io/noflo/graph) |  |  |  |
| 2026-10-08 06:05:32 | [noflo/noflo](https://jsr.io/noflo/noflo) |  |  |  |
| 2026-10-08 06:05:56 | [noflo/as-component](https://jsr.io/noflo/as-component) |  |  |  |
| 2026-10-08 06:06:15 | [noflo/fbp](https://jsr.io/noflo/fbp) |  |  |  |
| 2026-10-08 06:06:37 | [noflo/fbp-spec-runner](https://jsr.io/noflo/fbp-spec-runner) |  |  |  |
| 2026-10-08 06:06:56 | [noflo/loader-node](https://jsr.io/noflo/loader-node) |  |  |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
