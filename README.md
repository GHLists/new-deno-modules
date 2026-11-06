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

## Latest list — 2026-11-06 21:21 UTC

New modules created between 2026-11-06 20:19 UTC and 2026-11-06 21:21 UTC.

[Full CSV](data/new-deno-modules-2026-11-06T21-21-42-365731Z.csv)

| Created (UTC) | Package | Version | Score | Description |
| :------------ | :------ | :------ | ----: | :---------- |
| 2026-11-06 21:09:30 | [yaks/anthropic](https://jsr.io/yaks/anthropic) | 0.2.30 | 100 | Implements the model interface over Anthropic's Messages API, spoken over fetch… |
| 2026-11-06 21:09:34 | [yaks/benchmark](https://jsr.io/yaks/benchmark) | 0.2.30 | 70 | Named workloads, raw samples, JSON runs and explicit baseline ratchets, with pr… |
| 2026-11-06 21:09:37 | [yaks/cloudflare-mail](https://jsr.io/yaks/cloudflare-mail) | 0.2.30 | 100 | Cloudflare Email Sending and Email Routing at the portable mail boundary. |
| 2026-11-06 21:09:40 | [yaks/diagram](https://jsr.io/yaks/diagram) | 0.2.30 | 100 | Draws the entities a query selects, and the references between them, as SVG: a… |
| 2026-11-06 21:09:43 | [yaks/extension](https://jsr.io/yaks/extension) | 0.2.30 | 100 | A browser extension that lends a person's tab to their agent: reading and actin… |
| 2026-11-06 21:09:45 | [yaks/logic](https://jsr.io/yaks/logic) | 0.2.30 | 100 | A relational runtime in the miniKanren manner: unification over lists and objec… |
| 2026-11-06 21:09:48 | [yaks/phone](https://jsr.io/yaks/phone) | 0.2.30 | 94 | Phone numbers, provider selection, consent, texts and delivery outcomes in the… |
| 2026-11-06 21:09:52 | [yaks/pinnacle](https://jsr.io/yaks/pinnacle) | 0.2.30 | 64 | Pinnacle texting transport and authenticated webhook events for @yaks/phone. |
| 2026-11-06 21:09:55 | [yaks/resend](https://jsr.io/yaks/resend) | 0.2.30 | 94 | Resend sending, signed webhook receipts and incoming messages at the portable m… |
| 2026-11-06 21:09:58 | [yaks/speech](https://jsr.io/yaks/speech) | 0.2.30 | 94 | Speech to text, text to speech and speech to speech, each provider given as dat… |
| 2026-11-06 21:10:03 | [yaks/stage](https://jsr.io/yaks/stage) | 0.2.30 | 94 | Three.js scenes, effects, instancing, orbit cameras, picking and positional sou… |
| 2026-11-06 21:10:07 | [yaks/stripe](https://jsr.io/yaks/stripe) | 0.2.30 | 94 | Stripe's API over fetch, and the plans, shops and signed webhook doors it lends… |
| 2026-11-06 21:10:09 | [yaks/telnyx](https://jsr.io/yaks/telnyx) | 0.2.30 | 88 | Telnyx texting, calls and verified webhook events for @yaks/phone. |
| 2026-11-06 21:10:13 | [yaks/testing](https://jsr.io/yaks/testing) | 0.2.30 | 94 | Declare tests, check their results, and run test modules and examples in one ru… |
| 2026-11-06 21:10:17 | [yaks/voipms](https://jsr.io/yaks/voipms) | 0.2.30 | 88 | voip.ms texting transport, account numbers and inbound callbacks for @yaks/phon… |
| 2026-11-06 21:10:25 | [yaks/voxel](https://jsr.io/yaks/voxel) | 0.2.30 | 100 | Worker-safe voxel geometry, baked lamp light, chunk detail and heightfield char… |

## Data source

Data comes from the [JSR registry](https://jsr.io/) and its
[API](https://api.jsr.io/). Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by the Deno team or
Deno Land Inc.
