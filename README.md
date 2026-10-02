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

## Latest list — 2026-10-02 22:20 UTC

New modules created between 2026-10-02 21:22 UTC and 2026-10-02 22:20 UTC.

[Full CSV](data/new-deno-modules-2026-10-02T22-20-13-838616Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-10-02 21:27:48 | [tundraconnect/telegram](https://jsr.io/tundraconnect/telegram) | 0.1.1 | 100 | Typed Telegram Bot API client: send messages and fetch the bot's own identity. |
| 2026-10-02 21:27:53 | [tundraconnect/resend](https://jsr.io/tundraconnect/resend) | 0.1.0 | 100 | Typed Resend client: send single and batch transactional email with idempotency… |
| 2026-10-02 21:28:00 | [tundraconnect/google-web-risk](https://jsr.io/tundraconnect/google-web-risk) | 0.1.0 | 100 | Typed Google Web Risk client: check a URL against Google's malware, phishing an… |
| 2026-10-02 21:28:09 | [tundraconnect/urlhaus](https://jsr.io/tundraconnect/urlhaus) | 0.1.0 | 100 | Typed URLhaus (abuse.ch) client: look up URLs, hosts and payloads in the malwar… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
