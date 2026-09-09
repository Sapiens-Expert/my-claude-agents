---
id: source-coverage-audit-2026-08-31
type: fact
status: canonical
canonical: true
last_updated: 2026-08-31
---

# Full source incorporation coverage audit

## Result

Stage A is complete and reconciled. Every substantive source file is represented in its correct family map, every populated family map is centrally indexed, and the independently recomputed corpus and duplicate totals match the manifest. Stage B may begin with D0 classification.

| Check | Result |
| --- | ---: |
| Populated source families | 27/27 mapped and indexed |
| Substantive source documents | 511/511 mapped by filename |
| Unique files after exact hashing | 458 |
| Exact-duplicate groups | 37 |
| Redundant exact copies | 53 |
| File-type total | 448 PDF, 46 DOCX, 3 Markdown, 5 text, 8 VTT, 1 XLSX = 511 |
| Claim files in claim register | 12/12 |
| Frontmatter files parsed | 185/185 |
| Frontmatter YAML errors | 0 |
| Duplicate frontmatter IDs | 0 |
| Project schema validation | 18/18 passed |
| Broken local Markdown links | 0 |
| Formatting errors from `git diff --check` | 0 |

Guidance-only `README.md` files, `.DS_Store`, and the generated manifest are excluded from substantive-source counts.

## Reconciliation method

1. Enumerated every substantive file beneath `sources/` and independently calculated SHA-256 hashes.
2. Recomputed folder counts, file types, exact-duplicate groups, redundant copies, and unique-file total.
3. Matched every source basename against the source-family map assigned to its top-level folder.
4. Confirmed all 27 family maps are linked from the central source-map index.
5. Compared live totals across the manifest, source register, source-map index, and ingestion state.
6. Parsed repository frontmatter, checked unique IDs where present, validated project schemas, resolved local Markdown links, and ran whitespace/error checks.
7. Compared the claim directory with the canonical claim register.

## Corpus reconciliation

The original checkpoint contained 288 documents / 278 unique exact hashes. The expansion added 223 documents and 180 new unique hashes after cross-family and within-family reuse, producing 511 documents / 458 unique hashes.

All original files remain preserved. Exact deduplication controls extraction effort only; it does not delete evidence or collapse provenance. Different editions and near-duplicates remain separate unless their hashes are identical.

## Knowledge incorporation model

Stage A created semantic coverage rather than one summary per file. Sources feed canonical identity, brand, voice, knowledge, frameworks, projects, platforms, research, content, SOPs, decisions, and state nodes according to role. Family maps preserve provenance and authority limits.

Books and manuals were incorporated at skeleton depth: durable concepts, evidence limits, safety boundaries, and canonical destinations. This audit does not claim that every chapter, citation, case, exercise, or assertion has been extracted or independently validated; that is the purpose of Stage B.

## Controls preserved

- Medical, psychological, herbal, psychedelic, tax, legal, privacy, and safety material remains behind stronger authority, freshness, professional-scope, and referral gates.
- Personal, client, genetic, health, financial, and tax data remains private by default.
- Popular books, commercial frameworks, historical texts, traditional use, case studies, and personal experience do not automatically become evidence claims.
- Current operating records and active decisions continue to outrank historical plans.

## Stage B gate

The reconciliation prerequisite is satisfied. Start with D0: classify the 458 unique hashes into eligible books, non-book sources, exact duplicates, editions/near-duplicates, OCR or extraction issues, safety domains, and priority. Chapter-level extraction must follow the [deep-extraction program](../deep-extraction/README.md) and must not re-read redundant exact copies.

## Maintenance trigger

Repeat this audit whenever a substantive source is added, removed, renamed, or replaced. A changed hash or path requires manifest, duplicate, family-map, index, and affected-knowledge review before deep-coverage totals are updated.
