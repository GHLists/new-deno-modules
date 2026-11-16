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

## Latest list — 2026-11-16 19:20 UTC

New modules created between 2026-11-16 18:19 UTC and 2026-11-16 19:20 UTC.

[Full CSV](data/new-deno-modules-2026-11-16T19-20-12-896405Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-16 18:19:52 | [forgesworn/qr](https://jsr.io/forgesworn/qr) | 0.3.1 | 94 | Dependency-free QR encoder and decoder for TypeScript, browsers, workers and No… |
| 2026-11-16 18:53:44 | [nuxt-atelier/core](https://jsr.io/nuxt-atelier/core) |  |  | The Nuxt CMS with a visual builder for your own components |
| 2026-11-16 18:55:46 | [nuxt-atelier/editor](https://jsr.io/nuxt-atelier/editor) |  |  | Visual editor for Nuxt Atelier |
| 2026-11-16 18:56:49 | [nuxt-atelier/layer](https://jsr.io/nuxt-atelier/layer) |  |  | Optional starter layer for Nuxt Atelier: the module and the admin, with admin p… |
| 2026-11-16 18:58:05 | [nuxt-atelier/admin](https://jsr.io/nuxt-atelier/admin) |  |  | Headless admin composables and the default admin kit (crystal-neuo) for Nuxt At… |
| 2026-11-16 18:58:50 | [nuxt-atelier/devtools](https://jsr.io/nuxt-atelier/devtools) |  |  | Nuxt DevTools panels for Nuxt Atelier: schema, migrations, jobs and the admin |
| 2026-11-16 19:01:23 | [nuxt-atelier/i18n-micro](https://jsr.io/nuxt-atelier/i18n-micro) |  |  | nuxt-i18n-micro adapter for Nuxt Atelier |
| 2026-11-16 19:02:25 | [nuxt-atelier/i18n-nuxtjs](https://jsr.io/nuxt-atelier/i18n-nuxtjs) |  |  | @nuxtjs/i18n adapter for Nuxt Atelier |
| 2026-11-16 19:03:06 | [nuxt-atelier/auth-better-auth](https://jsr.io/nuxt-atelier/auth-better-auth) |  |  | Better Auth adapter for Nuxt Atelier |
| 2026-11-16 19:03:55 | [nuxt-atelier/ai](https://jsr.io/nuxt-atelier/ai) |  |  | Provider-agnostic AI assist adapter for Nuxt Atelier |
| 2026-11-16 19:05:14 | [nuxt-atelier/storage-s3](https://jsr.io/nuxt-atelier/storage-s3) |  |  | S3-compatible and R2 media storage driver for Nuxt Atelier |
| 2026-11-16 19:06:12 | [nuxt-atelier/storage-vercel-blob](https://jsr.io/nuxt-atelier/storage-vercel-blob) |  |  | Vercel Blob media storage driver for Nuxt Atelier |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
