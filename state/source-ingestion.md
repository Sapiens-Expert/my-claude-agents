---
id: source-ingestion-state
type: strategy
status: active
canonical: true
last_updated: 2026-09-06
---

# Source ingestion queue

## Goal

Incorporate the expanded source archive without exhausting daily or weekly model usage and without flooding VladOS with low-value summaries.

This program has two deliberately separate stages: Stage A builds complete semantic coverage and canonical structure; Stage B deep-reads each eligible unique book and adds chapter-level detail after Stage A is reconciled.

## Completed baseline

Phases 1–10 mapped the original 288 documents. A reconciliation correction establishes that checkpoint as 278 unique files after ten redundant exact copies. The new expansion adds 223 documents across nine new folders plus `transcripts/`, producing a live archive of 511 documents and 458 unique files after 53 redundant exact copies.

## Sequence

| Phase | Folder | Files | Processing depth | Primary destinations |
| --- | --- | ---: | --- | --- |
| 1 | Digital Vlad | 8 | **Complete** | Profile, identity, brand map, authority, skills |
| 2 | Management Consultant | 20 | **Complete** | Strategy, consulting, leadership, facilitation skills |
| 3 | Sales Manager | 22 | **Complete** | Sales knowledge, discovery, pipeline, negotiation SOPs |
| 4 | LinkedIn Guru | 28 | **Complete** | LinkedIn platform, social selling, DMs, content, metrics |
| 5 | COntent creation | 17 | **Complete** | Writing, UX content, copy, storytelling, content SOPs |
| 6 | FANATIC additions | 21 new | **Complete** | Branding knowledge, FANATIC capability and IP |
| 7 | O!Sapiens additions | 12 new | **Complete** | Audience, knowledge profile, positioning, offer/brand evidence |
| 8 | Psychedelic Coach | 29 | **Complete** | Integration, ethics, interactions, preparation, referral |
| 9 | AI Healer | 34 | **Complete** | Health knowledge, personal constraints, claims, clinical gates |
| 10 | Taxation Consultant | 32 | **Complete** | Spain/Cyprus/international tax research and professional referral |
| 11 | transcripts | 11 | **Complete** | Consent, client delivery, FANATIC decisions, Arkaya/network provenance |
| 12 | Workshops | 27 | **Complete** | Facilitation, learning design, workshop SOPs, internal framework mapping |
| 13 | Product Manager | 22 | **Complete** | Product discovery, business models, ICP, validation, membership, growth |
| 14 | AI coach | 20 | **Complete** | Coaching methods, MI, habits, focus, business and health scope |
| 15 | Text editor | 21 | **Complete** | Editing, style, clarity, content design, data storytelling, book writing |
| 16 | Nudger | 21 | **Complete** | Choice architecture, habits, motivation, scarcity, decisions, ethical nudging |
| 17 | Conscious marketer | 21 | **Complete** | Conscious business, category, narrative, content, persuasion guardrails |
| 18 | Psychologist | 24 | **Complete** | Psychology schools, attachment, IFS, trauma, diagnosis/referral boundaries |
| 19 | Arthritis Healer | 35 | **Complete** | Pain, movement, arthritis, nutrition, claims, red flags and referral |
| 20 | Plant medicine healer | 21 | **Complete** | Herbalism, pharmacognosy, interactions, toxicology, clinical boundaries |

## Per-phase deliverables

1. Folder manifest and duplicate/authority notes.
2. Source-family map.
3. New or revised knowledge and skill nodes.
4. Claims with evidence and safe wording where relevant.
5. Framework/project/SOP updates only when justified.
6. Conflicts, stale material, and open questions.
7. Validation of metadata and links.

## Cost controls

- One folder per turn unless the folder is very small.
- Process book metadata and contents before full text.
- Extract relevant chapters only.
- Never reprocess an exact duplicate.
- Prefer a single canonical synthesis over one note per book.
- Medical and tax claims receive targeted verification only when they affect a current decision.

## Completed checkpoint

The original 288 substantive documents remain covered by 17 indexed source-family maps. See the [checkpoint audit](../research/source-maps/coverage-audit-2026-08-30.md).

## Current expansion

Phases 11–20, repository-wide reconciliation, and D0 classification are complete. Stage A covers all 511 substantive documents / 458 unique files; D1 is next.

## Stage B — D0 complete, D1 ready

Phases 14–20, the final 511-document reconciliation, and D0 are complete. Begin D1 and retain one bounded domain batch per work cycle.

| Deep phase | Scope | Deliverable |
| --- | --- | --- |
| D0 | **Complete** | 458-hash ledger: 333 eligible, 125 excluded, duplicate/edition/OCR/domain/priority decisions |
| D1 | **Complete — 176 extracted + 13 user-skipped = 189/189 accounted** | Full chapter notes for core coaching, behavior, performance, workshops, product, strategy, sales, branding, content, and health works |
| D2 | Safety-sensitive books | Full chapter notes plus stronger claim/scope review for psychology, neuroscience, psychedelics, health, pain/arthritis, herbalism, and tax |
| D3 | Supporting/contextual books | Full notes for leadership, community, culture, history, memoir, and other contextual works |
| D4 | **In progress — 30/176 D1 works synthesized** | Concept graph, agreements/conflicts, upgraded knowledge and skills, claim-register updates |
| D5 | Final audit | Eligible books complete/excluded, chapter coverage, duplicate resolution, links, metadata, and knowledge provenance |

Method and completion rules: [deep extraction program](../research/deep-extraction/README.md).

## Active extraction priority

As of 2026-09-07, *Predictably Irrational* by Dan Ariely has completed D1 after local OCR of its complete 617-page scan. All 13 chapters are represented with replication-status, ethical-choice-design and manipulation safeguards, including explicit quarantine of the failed moral-reminder claim. This completes the initial D1 approach: **176 sources extracted and 13 explicitly skipped, accounting for all 189 eligible D1 works**. Next priority is the planned second, deeper extraction pass that adds claim-level granularity and cross-book synthesis. See [D1 progress](../research/deep-extraction/D1-PROGRESS.md#active-priority-override--strategy-marketing-and-linkedin).

The strategy/marketing pass now includes *The Copywriter's Handbook, Fourth Edition*. Its additive contribution is a sourced copy fact pack plus five joint controls—human context, evidence, measurement, compliance/safety and accountability—and a format router separating durable decision design from volatile channel mechanics. Response and digital attribution remain intermediate rather than truth or customer-value proof. D4 progress is **45/176 completed D1 works synthesized**. Next priority: *Letting Go of the Words, Second Edition*. See [D4 synthesis progress](../research/deep-extraction/D4-SYNTHESIS-PROGRESS.md).
