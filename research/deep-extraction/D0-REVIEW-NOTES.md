---
id: deep-extraction-d0-review-notes
type: fact
status: complete
canonical: true
last_updated: 2026-08-31
---

# D0 manual review notes

## Eligibility resolution

All 458 unique hashes have a resolved D0 disposition.

Nine short but complete or substantial works were promoted to deep extraction:

- *The Elements of Style*.
- *Crush It on LinkedIn*.
- *LinkedIn Personal Branding and Marketing*.
- *LinkedIn Social Selling Strategies*.
- *Lean Startup: How to Apply…*.
- *Outbound Sales, No Fluff*.
- *Evidence-Based Best Practices in Psychedelic Preparation and Integration*.
- *MAPS Integration Workbook*.
- PAT treatment recommendations dated in the filename.

The other 30 short PDFs in book-heavy families were explicitly excluded as internal reports/decks, third-party summaries, current-platform guides, tax leaflets/reports, workshop comparison sheets, incomplete copies, or non-book practice documents already covered by Stage A. They remain in the ledger with `short-summary-nonbook-or-incomplete` completeness and can be promoted later without changing their hash record.

## Edition and near-duplicate review

Exact duplicates already share one canonical extraction record. Filename-token review surfaced these non-exact candidates:

| Candidate pair/group | D0 decision |
| --- | --- |
| William James, *Principles of Psychology* and *Volume 2* | Separate volumes; retain both |
| Stanislav Grof, *Way of the Psychonaut*, Volumes One and Two | Separate volumes; retain both |
| IFS introduction and IFS therapy text | Related works, not duplicate editions |
| LinkedIn Messaging Guide and LinkedIn Sales Guide | Distinct works |
| *Pain Free Living* and *Pain Free*, revised second edition | Distinct Egoscue books; retain both |
| Aaker, *Brand Relevance* and *Brand Leadership* | Distinct works |
| Original *Nudge* and *Nudge: The Final Edition* | Different editions; retain separately and compare changes |

Near-duplicate detection is conservative. Bibliographic confirmation remains mandatory when an individual note begins, because filenames cannot reliably resolve all editions, translations, abridgments, or compilations.

## OCR and extraction review

Five PDFs had poor first-twelve-page extraction. Interior-page testing produced:

| Source | Disposition |
| --- | --- |
| *Predictably Irrational* | Eligible D1; zero interior text, OCR required |
| *Adaptogens: Herbs and Spices for Emotional…* | Eligible D2; negligible interior text, OCR required |
| *The Skilled Facilitator* | Eligible D1; zero interior text, OCR required |
| Psychedelic-therapy playlist PDF | Excluded non-book; OCR only if later promoted |
| Spain tax PDF `spain_2013_02_14_1st_en-66069c8d03087.pdf` | Excluded short document; verify current official source instead of OCR for book extraction |

OCR output must be checked against representative rendered pages before being used for chapter coverage or quotation.

## Priority result

- D1 core business/practice: 189 unique works.
- D2 safety-sensitive: 137 unique works.
- D3 supporting/contextual: 7 unique works.
- Excluded by corpus rule: 125 unique records.

D1 should proceed in small domain batches, beginning with foundational coaching and behavior-change works rather than creating 189 notes at once.
