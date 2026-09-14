---
id: telegram-archive-voice-analysis
type: research
status: active
canonical: true
brand: entheogen-expert
last_updated: 2026-09-14
---

# Telegram archive: structured database and voice-drift analysis

First analysis of the "Энтеогенный Ренессанс" Telegram archive (`sources/Telegram/archive/`, 2,199 posts, 2023-09-21 to 2026-08-30). Nobody had queried this corpus before; it existed only as flat files. This turns it into a queryable database and answers one concrete question: does the writing voice before 2025-01-01 differ from the writing voice after, and if so, how, so the earlier voice can be deliberately imitated rather than lost.

## What was built

- **Database**: `sources/Telegram/archive/telegram_archive.db` (SQLite), one row per post: `telegram_message_id, date, time_utc_local, channel, media, forwarded_from, merged_message_ids, reply_to_id, title, body, word_count, char_count, hashtag_count, link_count, emoji_count, period, source_file`. Indexed on `date` and `period`. Rebuildable any time the archive is re-parsed.
- **Build script**: `sources/Telegram/archive/scripts/build_database.py`, run after `parse_archive.py`. Pure standard library, idempotent, safe to re-run.
- **This paper**: methodology and findings below.
- **Companion voice guide**: [pre-2025 voice profile](../voice/entheogen-russian/pre-2025-voice-profile.md), the actionable output built from the findings here.

`period` splits the corpus at 2025-01-01: **pre-2025** (902 posts, channel's first 15 months) vs **post-2025** (1,297 posts, the following 20 months).

## Method

Word-frequency, hashtag, punctuation, emoji, and structural-marker counts computed per post and aggregated by period. Stopwords excluded from word frequency. "Opener" = first four words of a post's title line, counted only when it recurs more than once (filters out one-off headlines, surfaces template openings). Sample quotes pulled by filtering pre-2025 posts containing first-person markers (я/мой/мне) at 40-160 words, then hand-reviewed for voice, not cherry-picked for content.

Caveats: reactions, view counts, and full poll options aren't in the source export, so this only measures the text itself, not what performed. Emoji counts include some CJK/dingbat false positives from the regex range; treat emoji-per-post as directional, not exact. "Personal marker" regex counts are matched on standalone words, so first-person plural ("мы") is not separated from singular, meaning the true personal-narrative share is likely a bit higher than the singular-only numbers below.

## Findings

### 1. Posts got longer and more templated

| Metric | Pre-2025 | Post-2025 |
|---|---:|---:|
| Posts | 902 | 1,297 |
| Avg words/post | 151.2 | 215.5 |
| Avg chars/post | 1,330 | 1,903 |
| Posts with any hashtag | 28.9% | 87.1% |
| Posts using **bold** markdown | 4.3% | 9.0% |
| Posts with an explicit "источник" (source) callout | 10.6% | 23.2% |
| Emoji per post | 1.96 | 2.82 |
| "?" per post | 0.97 | 1.38 |

Post-2025 content converged on a repeatable shape: bolded headline, 3-6 bullet "основные выводы" (key findings), a hashtag block of 3-5 tags, a "Источник" link. That shape barely existed pre-2025 (10.6% source-callout rate, 28.9% hashtag rate) and became the default after (23.2%, 87.1%). This is consistent with a shift from writing as a person narrating what caught his attention, to summarizing found articles in a fixed template: a legitimate production efficiency, but a different voice.

### 2. Pre-2025 openers are narrative; post-2025 openers are announcements

Recurring pre-2025 openers: *"Тем временем в..."*, *"А что там..."*, *"На этой неделе..."*, *"Не могу не..."*, *"В дополнение к..."*. All mid-thought and conversational, assuming continuity with the reader.

Recurring post-2025 openers: *"🎙 Новый эпизод"*, *"🔥 НОВЫЙ ЭПИЗОД:"*, *"Всем привет!"*, *"🧠 Новое исследование:"*. Announcement headlines, capital-locked, emoji-flagged. "Всем привет!" (a generic greeting) appears 7+ times post-2025 and effectively never pre-2025.

### 3. Colloquial, self-deprecating asides are a pre-2025 signature that thinned out

Pre-2025 posts contain lines like *"запилил пост"*, *"меня закидывать помидорами"*, *"хрен с ним"*, and dramatic rhetorical openers structured as a skeptical reader's voice ("Что??!? Энтэогены лечат #мигрень??? Серьёзно?🤯" (2023-09-23); "Погоди-ка, гражданин. Вы что это?" (2023-09-24)). These read as one person thinking out loud, occasionally mocking his own audience's skepticism to make a point. Colloquialism markers are rare in absolute terms in both periods (0.4% vs 0.2% of posts by direct regex match), but they cluster specifically in the earliest months (the channel's first year) and the surrounding first-person passages carry the same register even without hitting the exact word list, so the regex undercounts the effect. This register does not appear in the post-2025 template-shaped posts.

### 4. Vocabulary shift: from "phenomenon" framing to "clinical evidence" framing

Pre-2025 top content words: психоделиков, лечения, исследование, энтеогены, псилоцибин, лсд, опыт, депрессии, терапия, mdma, птср.
Post-2025 top content words: энтеогены, псилоцибин, терапии, психоделики, исследование, опыт, эффект, mdma, важно, опыта, dmt, интеграции, эффект, часто, особенно, данные, источник, пациентов.

The post-2025 vocabulary adds "источник," "данные," "пациентов," "часто," "особенно": hedging and citation language typical of summarizing a paper or article rather than narrating a thought. This tracks with finding #1: more posts are structured article digests.

### 5. First-person presence held steady or grew slightly, but its function changed

Raw first-person marker rate (я/мой/моя/моё/мои/мне/меня/мной) is 25.7% pre-2025 vs 30.6% post-2025, so the pronoun didn't disappear. What changed is what it's attached to: pre-2025 first-person markers usually anchor a personal observation or decision ("Слушал на прогулке эпизод...", "Мой совет: если вы решили доверить свою психику 'терапевту'..."); post-2025 first-person markers more often anchor a framing sentence around a summarized study ("я решил разобрать это исследование"). The pronoun rate alone is not a reliable proxy for personal voice; the sample quotes in the companion guide matter more than this number.

## Interpretation

The channel's voice did not degrade so much as specialize into two unblended modes without anyone deciding to do that: (1) a person narrating, joking, and thinking out loud in front of an audience (dominant pre-2025), and (2) a structured science-digest template (dominant post-2025). Both are legitimate content types. The risk worth naming: if new content generation (including AI-assisted drafting) defaults to mode 2 because it's easier to template, the channel's original, harder-to-fake voice quietly disappears. That is the reason to lock in mode 1's fingerprint now, in the companion voice profile, before it's only reachable by digging through the archive.

## Reproducing this analysis

```
cd sources/Telegram/archive
python3 scripts/parse_archive.py      # rebuild posts/ + index.tsv from the HTML exports
python3 scripts/build_database.py     # rebuild telegram_archive.db from posts/
```

Query examples:

```sql
-- posts per month by period
SELECT substr(date,1,7) AS month, period, COUNT(*) FROM posts GROUP BY 1,2 ORDER BY 1;

-- longest pre-2025 posts (candidates for close reading)
SELECT date, telegram_message_id, word_count FROM posts
WHERE period='pre-2025' ORDER BY word_count DESC LIMIT 20;
```
