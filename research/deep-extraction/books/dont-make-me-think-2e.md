---
id: source-note-dont-make-me-think-2e
type: evidence
status: complete
canonical: false
last_updated: 2026-09-01
source_paths:
  - sources/COntent creation/Dont_make_me_think_-_Steve_Krug.pdf
domains: [usability, information-architecture, navigation, web-design, user-research, accessibility, content-design, privacy]
authority: classic-practitioner-web-usability-manual
extraction_status: complete
---

# Don't Make Me Think!, second edition — Steve Krug

## Bibliographic record

- Full title: *Don't Make Me Think! A Common Sense Approach to Web Usability*.
- Author/publisher/date: Steve Krug; New Riders, an imprint of Peachpit/Pearson; second edition, 2006.
- ISBN: 0-321-34475-8.
- Source: one 252-page English PDF; SHA-256 `9eb36a8e65476d6751ed1f695eba8b3989956a6691563003d1b15c8cbb55b9ca`.
- Completeness: preface, foreword, introduction, all 12 chapters, recommended reading, acknowledgments and index. Embedded text yielded about 41,990 words; no OCR was required.
- Authority: an influential practitioner synthesis based on repeated expert reviews and usability observation. It is not a systematic research review, current technical accessibility standard, contemporary mobile/app guide or statistically powered testing manual.

## Bottom line

- Krug's first law—**don't make me think**—means remove needless uncertainty about what something is, where a person is, what is clickable and what happens next. It does not mean remove necessary thought from consequential decisions.
- People usually scan, satisfice and muddle through rather than read everything, compare every option or learn the intended model. Design must make the first reasonable path safe, recognizable and recoverable.
- Strong pages expose an accurate visual hierarchy, use learned conventions, divide content into areas, signal interaction and suppress noise. Concision creates space for meaning but must not erase evidence, rights, risk or instructions users truly need.
- Navigation and home-page orientation are spatial/cognitive systems: identity, location, available routes, page name, local context and search must work together consistently.
- Frequent, small, early usability studies are primarily diagnostic. They replace opinion battles with observed behavior and prioritize high-impact fixes, but do not establish population preferences or experimental causality.

## Complete book coverage

| Unit | Complete contribution |
| --- | --- |
| Preface, foreword, introduction | Explains the second-edition scope, common-sense usability stance, brevity and principle-over-technology approach. |
| 1. Don't make me think! | Defines self-evidence/self-explanation and the cognitive cost of accumulated question marks; proposes clarity wherever a choice can reasonably be made obvious. |
| 2. How we really use the Web | Three observations: people scan rather than read, satisfice rather than optimize and muddle through rather than learn systems; designs should support successful recognition and recovery. |
| 3. Billboard Design 101 | Five scanability practices: clear visual hierarchy, conventions, defined areas, obvious clickability and low noise. |
| 4. Animal, vegetable, or mineral? | Choices are acceptable when they require little thought and offer enough context; eliminate ambiguity rather than blindly minimize clicks. |
| 5. Omit words | Remove low-value “happy talk” and unnecessary instructions; make the interface self-explanatory and retain only useful, task-relevant content. |
| 6. Street signs and Breadcrumbs | Builds navigation from site identity, sections, utilities, search, current-location indicators, page names, local navigation, breadcrumbs and tabs; requires consistent naming and visible hierarchy. |
| 7. The Home page | Home pages must rapidly communicate identity, purpose/value, scope, organization and starting points; protect orientation from promotional overload and avoid ambiguous entry points. |
| 8. Farmer and Cowman | Explains why preference-based “religious debates” are unproductive; roles and personal histories bias design opinions; resolve context-specific questions by observing intended users. |
| 9. Usability testing | Distinguishes focus groups from task observation; test early/often with small rounds, realistic tasks and broad observation; debrief immediately and prioritize major recurring problems. |
| 10. Usability as common courtesy | Introduces the reservoir of goodwill: needless demands, hidden information, punishment and amateur failures deplete trust; anticipation, candor, recovery and convenience replenish it. |
| 11. Accessibility | Accessibility is inseparable from usability; fix general confusion, learn from disabled users, use standards/semantic structure and implement keyboard/forms/text alternatives. Technical advice reflects 2006. |
| 12. Help! My boss wants me to… | Provides stakeholder arguments against unnecessary personal-data collection and distracting “sizzle”; request only necessary data and never let visual performance obstruct task success. |

## Core operating systems

### 1. Cognitive-friction audit

For every page/state, ask whether a reasonable person must pause to infer:

- What is this and who provides it?
- Where am I, and how did I get here?
- What can I do, and which option fits my goal?
- What is interactive, selected, required or unavailable?
- What will happen, cost or be shared if I continue?
- How can I go back, recover, undo or get help?

Classify each pause as necessary deliberation, useful learning or needless ambiguity. Remove the third category; protect the first two. Health, legal, financial, consent and irreversible decisions should support informed thought rather than engineer impulsivity.

### 2. Scanability and hierarchy gate

1. Importance is visible through semantic and visual prominence.
2. Related items are grouped; containment and nesting reflect actual relationships.
3. Conventional patterns are used unless evidence justifies teaching a better one.
4. Sections have clear boundaries without fragmenting one task.
5. Links, controls and current selection are perceivable across interaction modes.
6. Noise—competing emphasis, irrelevant decoration, promotional clutter and unnecessary words—is reduced.
7. The reading/listening order remains coherent without visual styling.

### 3. Navigation orientation test

A page should answer, where relevant: site/product identity; current page; current section/subsection; major routes; local alternatives; home/root; search; utilities; and the path back. Labels must match across entry point, destination title, breadcrumb, navigation and browser/document metadata. Home-page variation is allowed only when its relationship to the persistent system remains recognizable.

### 4. Home-page five-question test

Within a brief first look, can a new visitor answer:

1. What site/product/organization is this?
2. What can I do or obtain here?
3. What major content/functions exist and how are they organized?
4. Why is this relevant or trustworthy for me?
5. Where do I start for the most likely goals—including returning/signing in?

Stakeholder promotion consumes shared orientation capacity. Each promotional module needs an audience/task, evidence of value, expiry/owner and proof it does not materially damage primary journeys.

### 5. Lightweight diagnostic testing loop

1. Select a few high-risk questions, “get it” comprehension checks and realistic key tasks.
2. Test prototypes, competitors or live flows early; recruit people representative enough for the current question, including disability and edge-context coverage.
3. Facilitate one person at a time with neutral prompts; observe behavior and listen without teaching or defending.
4. Have the multidisciplinary team observe directly.
5. Debrief immediately: identify repeated blockers and surprising “head slappers,” then prioritize the largest low-cost/high-impact fixes.
6. Fix, retest and keep a regular cadence rather than waiting for launch.

Three or four participants can expose important issues in a round; they do not make the findings statistically representative. Use larger or specialized research when prevalence, subgroup comparison or consequential policy decisions require it.

### 6. Goodwill ledger

Depletes goodwill: hiding sought information, unnecessary steps/data, punishment for formatting, false urgency, unexplained errors, inaccessible paths, slow or fragile performance, marketing obstruction and failure to anticipate obvious needs.

Replenishes goodwill: state the key information, reduce effort, disclose requirements, accept reasonable input, preserve work, apologize honestly, explain delays, provide recovery/undo, answer likely questions, make support reachable and act in the person's interest.

Goodwill is a useful qualitative model, not a validated numeric reservoir. VladOS should operationalize it through task success, complaint themes, abandonment reasons, recovery success and trust research.

## Accessibility modernization

- Keep the durable insight that accessibility requires both a usable underlying experience and disability-specific design/testing.
- Replace 2006 implementation advice with current semantic HTML/platform APIs, WCAG and applicable law; JavaScript itself is not the issue—semantics, states, focus and input compatibility are.
- Test keyboard-only use, focus visibility/order, screen-reader structure/status, zoom/reflow, contrast, motion, captions/transcripts, input assistance, errors/recovery and cognitive load.
- Use headings, landmarks, labels and accessible names to make nonvisual scanning efficient; do not use alt text for decorative images or as a substitute for meaningful nearby content.
- Include disabled participants and relevant assistive technologies throughout research, not as a final validator exercise.

## Evidence and epistemic assessment

- The scan/satisfice/muddle model combines observed usability behavior with cited work, but the simplified trio is a design lens rather than a universal cognitive law.
- Examples demonstrate recurring failure modes; they do not quantify effect sizes or prove transfer to every product, device, culture or task.
- Small formative tests are strong for discovery and iteration, weak for prevalence estimates and fine-grained option comparisons. Krug explicitly positions them as issue-finding rather than proof.
- “Clicks don't matter” is best interpreted as path clarity outranking an arbitrary click target. Time, effort, errors, confidence, accessibility and consequence still matter.
- The accessibility chapter is historically important but technically obsolete in parts; current primary standards govern implementation.

## Current-use corrections and governance

### Keep as durable

- Remove needless ambiguity; design for scanning and satisficing; visible hierarchy and interaction; stable navigation/orientation; protect home-page purpose; observe users to settle contextual questions; regular formative testing; goodwill and data-minimization principles.

### Revalidate before use

- All 2006 websites, browser/search behavior, CSS/HTML/JavaScript prescriptions, print assumptions, link/tab/breadcrumb conventions and home-page examples.
- Participant-count and cadence choices against question/risk/resources.
- “Average user” framing; use inclusive, contextual populations rather than deficit language.

### VladOS additions

- **Safety:** clarity must surface uncertainty, contraindications, escalation and referral rather than merely speed action in health/psychedelic/psychology domains.
- **Privacy:** necessity, purpose, retention, sharing and consent govern every data request; fewer fields alone does not establish compliance.
- **Autonomy:** friction removal cannot enable dark patterns; decline, cancel, compare and exit require equivalent clarity.
- **Accessibility:** standards plus disabled-user evidence are release gates, not optional goodwill.
- **AI:** clearly distinguish generated/recommended content, provide source/uncertainty and correction or appeal for consequential outputs.
- **Research:** link each finding to participant/context/task/evidence, distinguish observation from inference and preserve contrary cases.

## Knowledge and skill mapping

| Extracted capability | VladOS destination at D4 | Reusable skill |
| --- | --- | --- |
| Cognitive-friction audit | `knowledge/content-strategy/`, `platforms/website/` | Classify and remove needless ambiguity while protecting informed decisions |
| Scanability hierarchy | `voice/writing-rules.md`, website/design standards | Align semantic, visual and interaction hierarchy to task priority |
| Navigation orientation | `platforms/website/`, `sops/content/` | Audit identity, location, routes, labels and recovery across pages |
| Home-page test | brand websites/project funnels | Evaluate identity, value, scope, trust and starting points under stakeholder pressure |
| Diagnostic usability loop | `research/audience-research/`, `templates/research-brief.md` | Run small neutral task studies, prioritize fixes and retest |
| Goodwill ledger | `knowledge/behavioral-psychology/`, support SOPs | Identify trust-depleting friction and design evidence-backed recovery |
| Data minimization argument | `AI-GOVERNANCE.md`, privacy/content briefs | Challenge unnecessary fields through task need, trust and truthful-data effects |
| Stakeholder debate resolution | `decisions/`, `sops/content/` | Replace preferences with explicit goals, hypotheses and observed evidence |

## Corpus synthesis

- Krug provides the clearest cognitive-friction and navigation lens; Redish adds deeper content planning, layering and content-specific testing.
- Podmajersky's dual-goal strategy, pattern library and measurement triangle make Krug's heuristics operational inside product teams.
- Fenton/Lee and Yifrah extend “common courtesy” into voice/tone, sensitive states and component-level recovery.
- D4 should incorporate Krug as the usability simplicity and lightweight-testing layer, not create a parallel UX-writing framework.

## Extraction boundary

This note covers the complete second edition and distinguishes durable principles from obsolete technical advice. It does not reproduce the copyrighted illustrations, annotated page reviews, testing transcript or sample stakeholder letters. Canonical promotion waits for D4 comparison.
