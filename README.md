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

## Latest list — 2026-10-04 08:20 UTC

New modules created between 2026-10-04 07:19 UTC and 2026-10-04 08:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-04T08-20-15-934484Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-04 07:29:14 | [stdext/event](https://jsr.io/stdext/event) |  |  | The event package contains extensions for events, such as CustomEventTarget |
| 2026-10-04 07:29:21 | [stdext/fs](https://jsr.io/stdext/fs) |  |  | Provides fs utilities and helpers, such as file cache |
| 2026-10-04 07:29:24 | [stdext/ffi](https://jsr.io/stdext/ffi) |  |  | Contains utilities for interacting with FFI, such as dlopen with remote file ca… |
| 2026-10-04 08:09:54 | [hobproj/hosting](https://jsr.io/hobproj/hosting) | 0.1.0 | 82 |  |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
