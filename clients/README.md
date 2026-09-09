---
id: clients-readme
type: principle
status: canonical
canonical: true
last_updated: 2026-08-30
---

# Clients

Session notes, agreement terms, and engagement history for active coaching clients, organized one subfolder per client. This is the delivery side of the O!Sapiens practice — distinct from `content/case-patterns/`, which holds de-identified public composites, never real named individuals.

New top-level folder — no prior convention existed in the repo for real, named, consented client data. Introduced here rather than reusing `content/case-patterns/`, since that folder's whole purpose is anonymized public content, a different function from operational delivery notes.

## Confidentiality — hard rule, not a preference

Everything here is bound by the confidentiality terms of the actual signed coaching agreement it derives from (IAC Code of Ethics; see the client's own `overview.md` for agreement specifics). This is real health, psychological, and professional information about a named person.

- **Never pull specifics from this folder into public content** — LinkedIn posts, newsletters, the book project, investor material — without the client's explicit consent. `content/case-patterns/README.md`'s rule (store only consented, de-identified composites) exists precisely so real session detail never surfaces recognizably; treat this folder as the reason that rule matters.
- **Never cross-reference one client's detail into another client's notes**, into `projects/linkedin-growth/` or any content-drafting work, even anonymized, without being explicitly asked.
- Aligns with existing repo norms: `sops/coaching/scope-and-referral.md` (state scope at intake, document risk/referral conversations) and `identity/boundaries.md` ("Client and personal health data require minimization and consent").

## Per-client structure (new convention — no prior schema existed in `templates/`)

```
[client-slug]/
  overview.md      Agreement terms, engagement timeline, goals, patterns across sessions
  sessions/         One file per session, chronological
```

Raw transcripts live in `../sources/transcripts/clients/[client-slug]/`, matching the taxonomy in `sources/README.md`.

Suggested frontmatter for `overview.md` and session files, following the repo's `id`/`type`/`status`/`canonical`/`last_updated` pattern plus client-specific fields: `client`, `engagement_status`, `consent` (what the client has/hasn't agreed can be used, and how). No existing template covers this — worth formalizing in `templates/` if a second client is added.

## Current clients

- **Tamaz Gadaev** — active, weekly cadence. See `tamaz-gadaev/overview.md`.
