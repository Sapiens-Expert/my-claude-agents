---
decision_id: DEC-2026-0909-01
type: decision
date: 2026-09-09
status: active
area: osapiens-linkedin-funnel
canonical: true
supersedes: []
---

# Reach becomes a secondary LinkedIn objective, via format not via imported hook mechanism

## Decision

LinkedIn post content may now target reach and top-of-funnel growth as a secondary objective, alongside qualified conversations (which stays primary). This is pursued through format diversification inside the existing, measured LinkedIn hook system, not by importing the VISP/ВИСП short-form-video hook formula, and not by increasing comment volume past the standing five-per-day cap.

## Context

Vlad asked whether the VISP hook technique (from the `reels-script` / Velizhanin short-form video methodology, elsewhere scoped in VladOS to the Russian-language `osapiens_expert` Instagram account) should be used to expand the LinkedIn funnel. Two things needed resolving: whether "expand the funnel" meant better conversion of the current audience or a deliberate override of `state/NOW.md`'s "conversion before audience expansion" stance, and whether VISP itself fits LinkedIn's medium at all. Asked directly, Vlad confirmed the goal is top-of-funnel reach growth, not just better conversion of the current audience.

## Alternatives considered

- Status quo, conversion-first only. Rejected: Vlad explicitly asked for reach growth.
- Apply the VISP/video-hook formula to LinkedIn text posts. Rejected: mechanistically mismatched (a 2 to 3 second audiovisual pattern interrupt has no equivalent in a text post judged by a "see more" click), and the channel already runs its own hook system with four weeks of measured performance data that a video-hook import has no track record against.
- Increase LinkedIn comment volume as the reach lever. Rejected: contradicts `decisions/active/2026-07-11-reduce-linkedin-comment-volume.md`, which Vlad was not asked about and did not confirm overriding.
- Format diversification (carousels, personal-data posts) inside the current hook system. Adopted: the content library's own audit already flags this as the highest-yield, most underused lever, and it requires no new hook framework.

## Rationale

The content library's own analytics (`sources/Linkedin/OSapiens_LinkedIn_Content_Library.md`, sections 1.3 and 3) found: 86.9% of profile appearances come from comments, not posts, so posts operate on the remaining roughly 11%; the reach ceiling is a distribution and audience-composition problem rather than a content problem (much of the 16,000+ follower base is in Moscow and India and is not the buyer); the one observed reach-multiplier mechanism is engagement-rate-triggered algorithmic redistribution (one post went 31 to 294 impressions, +848%, after a week), which rewards save and share-worthy single-mechanism content, not hook novelty; and carousels are the single highest-yield format measured, with only one ever published. Given that, the fastest legitimate path to more reach is more of the already-identified, underused high-yield formats, not a hook vocabulary imported from a different medium and channel.

## Consequences

Post cadence, the locked voice rules, and the Section 1.3 hook ranking stay unchanged. What changes going forward: carousel and personal-data-post formats get explicit priority in the content queue; saves and second-wave distribution get tracked as reach signals, not just conversation yield. Comment targeting and volume stay as they are (five per working day, senior European founder and operator feeds) unless a separate decision changes that.

## Evidence and assumptions

Verified: the hook ranking and the 86.9%-from-comments finding, both from the content library's own four-week audit (self-reported inside that document, not independently re-verified in this session).

Assumption: the audience-composition problem (Moscow and India-heavy follower base) has not changed materially since that audit. If wrong: reach gains from better content will be smaller than the audit implies, because the underlying audience still is not the buyer.

## Revisit trigger

Revisit if carousel or personal-data-post formats do not show measurably better reach or save rates after six to eight posts, or if the five-per-day comment cap turns out to be the actual binding constraint on reach rather than post format.
