---
id: telegram-archive-readme
type: fact
status: active
canonical: true
last_updated: 2026-08-31
brand: entheogen-expert
---

# Telegram channel archive: "Энтеогенный Ренессанс"

An organized, searchable archive of every message in Vlad's Telegram channel, generated from a Telegram Desktop HTML export. Built to make it possible to find and pull one specific past publication, not to browse the raw export.

## Source

`../messages.html`, `../messages2.html`, `../messages3.html`: Telegram Desktop's own export format, three sequential files covering **2023-09-21 (channel creation) through 2026-08-30**, contiguous with no gaps. The channel has been renamed at least twice over that span (service-message history shows "TabooLifting" at creation, later "Психоделическое просвещение," later "Психоделический Ренессанс," current name "Энтеогенный Ренессанс") — a post's channel name at time of writing isn't tracked per-post, only the current name in each file's frontmatter.

## Structure

- `posts/<year>/<date>-<telegram-message-id>.md`: one file per publication. 2,199 files total.
- `index.tsv`: one row per publication, columns `date, time, id, media, forwarded, file, title_snippet`, sorted chronologically. Tab-separated to match this repo's existing large-list convention (see `research/deep-extraction/corpus-ledger.tsv`).

Each post file has frontmatter (telegram message id, date, exact timestamp, media type if any, forwarded-from source if any, reply-to id if any) followed by the cleaned message text as the body.

**What counts as one "publication":** Telegram groups consecutive messages from the same sender with no gap under one visual header in its own UI (marked `joined` in the export). This archive follows that same grouping: a joined continuation is merged into the text of the message immediately before it, and the file records which raw message ids were combined (`merged_message_ids` in frontmatter) so nothing is lost, just presented as one coherent post instead of several fragments.

## How to find a specific publication

- **By keyword:** `grep -ril "keyword" posts/` from this directory, or grep against `index.tsv`'s `title_snippet` column for a faster first pass.
- **By date:** browse `posts/<year>/` directly, or filter `index.tsv` on the `date` column.
- **By Telegram message id:** the filename always ends in `-<id>.md`.

## Known limitations

- Captions and text are fully captured; the images, videos, voice notes, and files themselves are not copied here, only a presence flag and best-effort type (`photo`, `video`, `poll`, `audio_file`, `file`, `voice_message`) in frontmatter.
- Poll messages capture the question text only, not the full option list or vote counts.
- Reactions and view counts from the export are not carried into these files.
- `forwarded_from` captures the forwarded source's display name where Telegram's export exposes one; it doesn't distinguish a forward with added commentary from a bare repost.
- This is a first pass built with a regex-based parser (pure Python standard library, no dependencies). It ran clean against all 3,319 raw message blocks with zero parse warnings and zero id collisions on 2026-08-31, but if the export format shifts in a future Telegram version, re-running may surface new edge cases; check stderr output when re-running.

## Reproducing or updating this archive

`scripts/parse_archive.py`, run from anywhere: `python3 scripts/parse_archive.py`. It reads the three source HTML files in `../`, rebuilds `posts/` and `index.tsv` from scratch each time. Re-run it whenever a fresher export replaces the source files; it's idempotent and safe to overwrite.

## Structured database and voice analysis

`telegram_archive.db` (SQLite) is a queryable rebuild of every post in `posts/`, one row each, with word/hashtag/link/emoji counts and a `period` column split at 2025-01-01 (`pre-2025` / `post-2025`). Built by `scripts/build_database.py`, run after `parse_archive.py`; rebuilds the database and `voice-drift-stats.json` from scratch each time.

This was built to answer a specific question: does the channel's voice before 2025 differ from after, so the earlier voice can be deliberately imitated. Findings and method: [research/telegram-archive-voice-analysis.md](../../../research/telegram-archive-voice-analysis.md). The resulting imitation guide: [voice/entheogen-russian/pre-2025-voice-profile.md](../../../voice/entheogen-russian/pre-2025-voice-profile.md).

## Related, and not to be confused with this archive

- `../../../projects/entheogenic-renaissance/` describes an "existing podcast/content asset" with an episode/guest library. That description doesn't match this channel (a text-post channel, not a recorded-conversation format), and its own `episode-library.md` says no actual episode inventory was ever supplied. Worth Vlad confirming directly whether that project file is describing something separate from this Telegram channel, or whether it was a misclassification carried over from thin source material — flagged here rather than silently reconciled, since guessing wrong in either direction would misfile real content.
- `~/Claude/Entheogenic Renaissance/AGENT_SPECIFICATION.md`: a separate, previously-built specification for a *daily post-generation* agent (PubMed-driven, not archive-retrieval), based on an earlier PDF export of this same channel from around February 2026. That spec is about writing new posts; this archive is about retrieving old ones. Complementary, not overlapping.
