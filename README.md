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

## Latest list — 2026-10-06 10:19 UTC

New modules created between 2026-10-06 09:21 UTC and 2026-10-06 10:19 UTC.

[Full CSV](data/new-deno-modules-2026-10-06T10-19-54-347963Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-06 10:18:12 | [storyshelf/affected](https://jsr.io/storyshelf/affected) |  |  | Affected capture for StoryShelf: dependency-graph tracing that selects the stor… |
| 2026-10-06 10:18:17 | [storyshelf/auth](https://jsr.io/storyshelf/auth) |  |  | Better Auth engine for StoryShelf: opaque DBAdapter bridge, shelf factory, and… |
| 2026-10-06 10:18:21 | [storyshelf/db-mysql](https://jsr.io/storyshelf/db-mysql) |  |  | MySQL/MariaDB database adapter for StoryShelf (mysql2 + Drizzle, PlanetScale/Ti… |
| 2026-10-06 10:18:26 | [storyshelf/notify-chat](https://jsr.io/storyshelf/notify-chat) |  |  | Chat notification providers for StoryShelf (Slack and Teams incoming webhooks). |
| 2026-10-06 10:18:29 | [storyshelf/notify-email](https://jsr.io/storyshelf/notify-email) |  |  | Email notification transport for StoryShelf (SMTP, Mailpit, log, HTTP APIs). |
| 2026-10-06 10:18:32 | [storyshelf/observability](https://jsr.io/storyshelf/observability) |  |  | StoryShelf observability: OpenTelemetry tracing, metrics, and log correlation o… |
| 2026-10-06 10:18:35 | [storyshelf/queue-azure](https://jsr.io/storyshelf/queue-azure) |  |  | Azure capture queue adapter for StoryShelf: Storage Queues or Service Bus. |
| 2026-10-06 10:18:39 | [storyshelf/queue-gcp](https://jsr.io/storyshelf/queue-gcp) |  |  | GCP capture queue adapter for StoryShelf: Cloud Pub/Sub. |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
