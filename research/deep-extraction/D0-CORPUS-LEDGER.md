---
id: deep-extraction-d0-ledger
type: fact
status: complete
canonical: true
last_updated: 2026-08-31
---

# D0 corpus classification

## Result

The reconciled 511-document archive resolves to 458 SHA-256 records. One canonical extraction path is selected per hash; all 39 duplicate groups and 55 redundant copies resolve to those same records.

The machine-readable source of truth is [corpus-ledger.tsv](corpus-ledger.tsv). Eligibility is resolved; bibliographic fields remain provisional until each eligible work starts. Manual decisions and near-duplicate/OCR review are recorded in [D0 review notes](D0-REVIEW-NOTES.md).

| Classification | Unique records |
| --- | ---: |
| Deep eligible | 334 |
| Needs D0 manual review | 9 |
| Excluded by corpus rule | 2574 |
| **Total unique hashes** | **2917** |

## Extraction queue

| Phase | Unique records |
| --- | ---: |
| D1 — core business/practice | 189 |
| D2 — safety-sensitive | 137 |
| D3 — supporting/contextual | 8 |
| D0 manual review | 9 |
| Excluded | 2574 |

## Record types

- `book`: 298
- `dataset`: 1
- `internal-document`: 2375
- `internal-or-research-pdf`: 32
- `manual/reference`: 36
- `other`: 9
- `short-nonbook-summary-or-incomplete`: 153
- `transcript`: 13

## Extraction quality

- PDFs provisionally requiring OCR or repair: 5.
- `good`/`sparse`/`poor` is based on extractable characters from the first twelve pages and must be rechecked at book level.
- Short PDFs in book-heavy families were manually promoted or excluded; no D0 eligibility decision remains unresolved.
- DOCX, Markdown, spreadsheets, transcripts, and PDFs in operating/research families are excluded from chapter-level book extraction unless manually promoted.

## Fields

Each row records full hash, canonical path, all duplicate paths, families, inferred title, type/pages, extractability, eligibility/phase, domain, safety level, provisional authority, bibliographic-review state, and extraction status.

## D0 completion

- All `needs-review` eligibility rows are resolved.
- Exact duplicates share one record; likely editions, volumes, and near-duplicates were reviewed separately.
- OCR candidates were tested on representative interior pages.
- Exclusions and promotions remain explicit in the ledger.
- Title, author/editor, edition/year, language, completeness, and authority must be confirmed at the start of each D1–D3 book note.
