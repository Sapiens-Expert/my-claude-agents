---
id: podcast-archive-readme
type: fact
status: active
canonical: true
last_updated: 2026-08-31
brand: entheogen-expert
---

# Podcast transcript archive

An organized, searchable archive built from the subtitle PDFs in `../Subs/`, one clean text file per episode plus a chronological/searchable index. Two distinct series are covered.

## What's in here

- **Энтеогенный Ренессанс (main show)**: 102 episodes, numbered 1 through 110 with gaps. Russian-language. This is the same brand as the Telegram channel archived at `../../telegram/archive/`.
- **The Other Russian**: 24 episodes, numbered 1 through 24. English-language. Filenames read "Vlad's podcast. Episode NN," suggesting Vlad hosts this one too, but nothing in VladOS currently documents this show, its brand, its relationship to entheogen.expert, or Vlad's role on it (the opening lines of episode 1 are first-person, consistent with hosting rather than guesting, but that's an inference, not a confirmed fact). **Needs Vlad's confirmation before this gets classified or linked into any brand strategy.**

## Source format

The PDFs are exported SRT-style caption files (numbered index, timestamp line, caption text, repeated), not flowing transcripts. The parser strips the index and timestamp lines and rejoins the caption fragments into continuous paragraphs, breaking after sentence-ending punctuation. This is a mechanical rejoin, not a proofread transcript: caption-boundary artifacts (an odd line break, a word split awkwardly) are possible and expected.

## Structure

- `posts/entheogenic-renaissance/EP<NNN>-<slug>.md`
- `posts/the-other-russian/EP<NNN>-<slug>.md`
- `index.tsv`: series, episode number, title, word count, file path, original source filename. Tab-separated, one row per episode.

Each post file's frontmatter has empty `guest`, `date`, `themes`, and `permissions: unconfirmed` fields on purpose. Those need Vlad's input; nothing here is guessed. Backfilling `themes` per episode from a proper read (not just the filename title) would need to happen deliberately, not silently.

## How to find a specific episode

- **By topic, if the filename already names it** (most do: "Кетамин," "Мифы," "Плацебо," etc.): scan `index.tsv`'s title column or browse the folder directly.
- **By keyword inside the transcript:** `grep -ril "keyword" posts/` from this directory.
- **By episode number:** filenames are zero-padded, `EP017-...`, `EP102-...`.

## Items flagged for review, not resolved here

- `0102.pdf`: word count is close to but not identical to `EP102. Приходи поговорить.pdf`, so this is either an alternate cut, a re-record, or a stray duplicate. Filed as `EPunk-0102.md`, not merged into EP102, until Vlad says which it is.
- `Biohacking.pdf`: no episode number in the filename. Filed as `EPunk-Biohacking.md`. May duplicate the already-numbered `EP 82. Biohacking.pdf`, worth checking.
- `EP57. Bad Trip.pdf` and `EP57. Bad Trip copy.pdf`: both map to episode 57. Both processed and kept as separate files pending Vlad confirming which is canonical.
- `Sapiens OS. Дисфунцкиональное общество.pdf`, `Как внедрять привычки.pdf`, `Стрим. Результаты количественного исследования.pdf`: no episode number, likely bonus/special content (one is explicitly a livestream, "Стрим"). Filed under the main show with `episode_number: null`.
- `Archive.zip` (both the one directly in `Subs/` and the one inside `Subs/The Other Russian/`): not processed. Filenames inside decode as mangled Cyrillic (a zip encoding issue, not a content problem), and every episode number visible in the zip's file listing already exists as a clean loose PDF alongside it. Treated as a redundant backup, not a distinct source.

## Reproducing or updating this archive

`python3 scripts/parse_podcast_archive.py` from this directory (or anywhere, paths are relative to the script). Requires the `pdftotext` command (poppler-utils, already present on this machine). Rebuilds `posts/` and `index.tsv` from scratch each run; safe to re-run after adding new episode PDFs to `../Subs/`.

## Related

- `../../telegram/archive/`: the companion Telegram channel archive for the same "Энтеогенный Ренессанс" brand.
- `../../../projects/entheogenic-renaissance/episode-library.md`: VladOS's own episode-library page, now pointed at this archive instead of sitting empty.
