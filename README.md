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

## Latest list — 2026-11-11 19:21 UTC

New modules created between 2026-11-11 18:21 UTC and 2026-11-11 19:21 UTC.

[Full CSV](data/new-deno-modules-2026-11-11T19-21-55-462071Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-11 18:37:52 | [ihavethatonvinyl/lexicons](https://jsr.io/ihavethatonvinyl/lexicons) | 0.1.0 | 0 |  |
| 2026-11-11 18:45:37 | [kehto/rate-limit](https://jsr.io/kehto/rate-limit) |  |  |  |
| 2026-11-11 19:09:59 | [jund-fauz/j-kompact](https://jsr.io/jund-fauz/j-kompact) | 0.3.0 | 47 | A utility library for manipulating data in JavaScript / TypeScript. Works on No… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
