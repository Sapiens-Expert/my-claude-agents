---
decision_id: DEC-2026-0830-02
type: decision
date: 2026-08-30
status: active
area: offer-and-pricing
canonical: true
supersedes: []
---

# Confirm diagnostic price, category name, offer structure, and course-tier status

## Decision

- **Executive Performance Diagnostic price: €350.** Confirmed by Vlad directly, resolving a 4x internal discrepancy in pre-VladOS material (€350 in one source, €1,500 in another).
- **Category name: Executive Biology.** Not "Executive Healthspan" — resolves the conflict between VladOS's own index/state files (which already said Executive Biology) and `sources/Personal/EXECUTIVE_HEALTHSPAN_VOICE_MANUAL.md`'s copy-paste system prompts (which asserted "Executive Healthspan" as the category). The raw source file is left unedited per the provenance rule (never edit a source to agree with a synthesis) — `voice/executive-healthspan/voice-manual.md` carries the correction instead.
- **Performance Reset is an upsell, following the diagnostic — not the flagship/entry offer.** Confirms the funnel already stated in `brands/osapiens/messaging.md` ("Conversation → fit call → paid diagnostic → written protocol → Performance Reset") and in `projects/executive-coaching/offer.md`. The pre-VladOS voice manual's claim that Performance Reset is the flagship offer was wrong.
- **Sapiens OS course tiers are active, live on the Skool platform — not deferred.** Includes a tier called "Habits" in addition to 101/Core/Deep. This **overturns** `brands/osapiens/messaging.md`'s prior "inactive hypotheses" framing and `projects/executive-coaching/offer.md`'s "Deferred assets" section for courses specifically — those were wrong, not the pre-VladOS material. Pricing for the tiers is still unconfirmed.

## Context

A cross-check between pre-VladOS local knowledge, the `/osapiens` skill, and VladOS itself (2026-08-30) surfaced five unresolved money/naming contradictions. Vlad resolved four of them directly in conversation. See `platforms/linkedin/current-audit.md` and this decision's companion note in `voice/executive-healthspan/voice-manual.md` for related findings from the same audit.

## Alternatives

Leaving the price/category/offer-status ambiguous and continuing to write `[NEEDED: confirm]` in place of a number — rejected, since Vlad gave a direct, confident answer and the whole point of resolving a flagged contradiction is to stop treating it as open.

## Rationale

Vlad's live instruction is rank 1 in the authority order (per `~/.claude/CLAUDE.md`) — it overrides both the older material and VladOS's own prior "inactive"/"unconfirmed" framing where they conflict with what he just stated directly.

## Consequences

- `projects/executive-coaching/offer.md`, `brands/osapiens/messaging.md`, and `voice/executive-healthspan/voice-manual.md` updated to match.
- The `/osapiens` skill's `references/business-facts.md` (outside this repo, at `~/.claude/skills/osapiens/`) also needs the same correction — flagged separately since it's not part of VladOS.
- Skool-platform course tiers (101/Core/Deep/Habits) should now be treated as a real, live secondary offer surface when relevant to a conversation — not something to describe as dormant or hypothetical.

## Evidence and assumptions

Course-tier pricing itself remains unconfirmed — only "active, on Skool" is settled. Treat any specific tier price as `[NEEDED: confirm]` until stated directly.

## Revisit trigger

If course-tier pricing is confirmed, or if the Skool offering's status changes.
