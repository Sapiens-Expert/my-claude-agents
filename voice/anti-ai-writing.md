---
id: voice-anti-ai-writing
type: principle
status: canonical
canonical: true
last_updated: 2026-08-31
---

# Anti-AI-writing toolkit

Operational summary of `sources/Anti AI writing/Anti-AI-Writing_Field_Guide.docx` (a cited research compilation, prepared 2026-08-31). Read that source for the full academic backing, the platform-by-platform tell lists, and 30 worked before/after examples. This file holds the rules extracted from it that now govern production, alongside `voice-rules.md`, `writing-rules.md`, and `banned-patterns.md`.

## The core finding

No single word, em dash, or polished sentence proves a text is AI-written. What actually reads as generated is a *cluster*: familiar vocabulary, familiar sentence frames, every angle covered at equal weight, mechanically tidy formatting, and hedging that never connects to a real risk. The common thread is low selection pressure — the text doesn't show that anyone chose what mattered and cut the rest. The fix is not fake typos or forced casualness. It's editorial judgment: decide what matters, name the constraint, support the load-bearing claim, and let rhythm follow meaning.

## Highest-value checks, ranked

In order of how strongly each one reads as generated:

1. A dense cluster of inflated/abstract vocabulary (crucial, pivotal, holistic, robust, seamless, landscape, realm) — weak alone, strong in combination.
2. A sentence template repeated across the piece ("not just X, but Y," "whether X or Y," three "It's not X, it's Y" paragraphs in a row).
3. Generic significance inflation — a claim of importance with no mechanism behind it.
4. Redundant exposition — restating the same idea in different words.
5. Completeness without prioritization — ten evenly-weighted points instead of the two that matter.
6. No situated specificity — a claim that never names a date, threshold, population, or mechanism.
7. Mechanically balanced tone ("both approaches offer unique benefits and challenges") where a real recommendation belongs.
8. Textbook-respectful disagreement ("I appreciate your perspective, however...") instead of a boundary condition.
9. Participial significance tails: "…, highlighting the importance of…", "…, underscoring…", "…, ensuring…".
10. Forced rule-of-three, bold-label bullet stacks, and headings for every paragraph.

Weak/near-worthless signals on their own, despite common belief: em dash frequency, curly quotes, and over-polished grammar. Current comparisons even found Claude using *more* em dashes than professional human writers in tested samples, so treat dash-hunting as close to noise. Density and clustering are what matter, not any single mark.

## Phrases to cut or replace by default

Preambles and false closure: "in today's fast-paced world," "at its core," "it's important to note," "the answer lies in," "this is where X comes in," "let's explore," "here's why."

Vague benefit frames: "plays a crucial role," "by understanding X, you can Y," "more than just," "the key is to," "unlock your potential."

Facilitation/empty-quality verbs and adjectives, used without a concrete referent: foster, leverage, empower, unlock, utilize, holistic, robust, seamless, dynamic, transformative, game-changing, ever-evolving.

Full caution list with "use only when X is true" conditions: see the source document, section 5.

## Self-check before publishing

For any paragraph that's supposed to be doing real work, ask:

- What does this add that the line before it didn't?
- Could this sentence appear unchanged in any other piece on this topic?
- Is there a mechanism connecting the cause to the outcome, or just a positive association?
- What constraint, cost, or tradeoff is being acknowledged?
- What would make this claim false?
- Is the caveat here changing the decision, or just protecting the writer?
- Does the ending advance the thought, or repeat the opening?

If a paragraph fails several of these, rewrite from the claim outward. Don't just swap in different synonyms.

## Diagnostic score (for a genuinely uncertain draft)

Score 1 (clean) / 3 (noticeable) / 5 (dominant) on each: lexical AI texture, repeated sentence-pattern texture, over-structured formatting, generic-smooth tone, semantic genericness (universal truths vs. load-bearing claims), over-completeness (no prioritization), generic hedging, absence of a real point of view, lack of situated specificity, platform mismatch.

Total: 10-18 is fine as-is. 19-28 needs a selective edit pass. 29-38 needs a structural rewrite, not a word swap. 39-50 means start over from a sharper brief. This measures editorial risk, not proof of authorship, use it as a gate, not an accusation.

## Where this plugs in

- `voice-rules.md` VOICE-016 through VOICE-023 are the atomic rules pulled from this toolkit.
- The `/content-qc` skill's gate 8 (voice, self-edit pass) and the `osapiens` skill's `references/voice.md` §8 should apply the self-check and, for a draft that still reads uncertain after one pass, the diagnostic score above.
- Platform-specific tells (LinkedIn line-break theatrics, Instagram inspirational abstraction, TikTok "did you know" hooks, YouTube padded recaps, sales-page adjective stacks) are in the source document, section 11, and should inform `channels.md` and the platform strategy files as they're revised, rather than being copied wholesale here.
