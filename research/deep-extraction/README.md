---
id: deep-extraction-program
type: strategy
status: active
canonical: true
last_updated: 2026-08-31
---

# Deep extraction program

## Purpose

The initial ingestion pass builds the skeleton: complete file coverage, authority classification, major concepts, canonical destinations, duplicate reuse, and safety gates.

Phases 14–20, the 511-document reconciliation, and D0 classification are complete. The deep pass is ready for D1 chapter extraction. It adds chapter-level granularity and cross-source synthesis without replacing the original source maps.

D0 is complete: [the corpus ledger](D0-CORPUS-LEDGER.md) resolves 458 hashes into 333 eligible works and 125 exclusions, with [manual review notes](D0-REVIEW-NOTES.md). D1 is ready to proceed in bounded domain batches.

D1 progress is tracked in [D1-PROGRESS.md](D1-PROGRESS.md). The first completed note is [Motivational Interviewing, fourth edition](books/motivational-interviewing-4e.md).

## Corpus rule

- Process each unique book or substantial manual once, regardless of how many folders contain it.
- Link every duplicate path to the same extraction note.
- Exclude transcripts, short internal records, generated summaries, and operating documents already better represented by their source-family map unless explicitly promoted for deep review.
- Record edition, language, publication date, completeness, extraction quality, and authority before reading.
- For scanned or poorly extractable books, perform OCR and verify representative pages before analysis.

## Per-book output

Each eligible book receives one note under `research/deep-extraction/books/` using [the book-extraction template](../../templates/book-extraction.md). The note must contain:

1. Bibliographic and provenance record.
2. Full chapter/section coverage ledger.
3. Central thesis and argument structure.
4. Key concepts with the author's meaning and relationships.
5. Named frameworks, models, processes, and decision rules.
6. Claims, evidence offered, counterclaims, and uncertainty.
7. Examples/cases and whether they are illustrative or evidentiary.
8. Limitations, assumptions, dated elements, conflicts of interest, and safety issues.
9. Contradictions and complementarities with other VladOS sources.
10. Applications to identity, brands, knowledge, frameworks, projects, content, SOPs, skills, or claims.
11. A concise “do not infer” section.

## Knowledge integration rule

Book notes remain in research. Concepts move into `knowledge/` only after comparison with other sources and removal of author-specific overclaiming. Proprietary VladOS frameworks may be strengthened only when the derivation is explicit and does not appropriate a third party's named IP.

Use this chain:

`unique book → deep extraction note → cross-book concept synthesis → canonical knowledge → framework/project/SOP application`

## Reading standard

“Deep extracted” means every substantive chapter was processed, not merely the contents or selected passages. Chapter coverage can be satisfied through direct full-text reading plus targeted rereading of high-value sections. Record unreadable, missing, appendix-only, reference-only, or deliberately excluded sections.

## Evidence and copyright

- A book's assertions remain the author's claims until independently supported.
- Popular, commercial, memoir, alternative-health, and historical books receive explicit authority limits.
- Medical, psychological, herbal, legal, and tax claims must not become operational guidance from a book alone.
- Prefer paraphrase and concept indexing. Store only short quotations necessary for analysis, with page/location and rights awareness.

## Priority order

After corpus classification, process in bounded domain batches:

1. VladOS core: coaching, behavior change, executive performance, facilitation, product, strategy, sales, branding, and content.
2. Safety-sensitive foundations: neuroscience, psychology, psychedelics, health, arthritis/pain, plant medicine, and taxation.
3. Supporting and contextual works: leadership, culture, community, political economy, memoir, and historical sources.

Within each batch, prioritize foundational/authoritative works, then counterpoints, then practitioner/commercial applications.

## Completion criteria

- Every eligible unique book has a complete note or a documented exclusion.
- Every chapter has a coverage status.
- Duplicate paths resolve to one note.
- High-consequence claims are registered or explicitly rejected.
- Cross-book contradictions are synthesized by domain.
- Canonical knowledge files record material upgrades and provenance.
- Repository validation and a deep-extraction coverage audit pass.
