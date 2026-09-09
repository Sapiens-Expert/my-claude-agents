#!/usr/bin/env python3
"""
Convert the podcast subtitle PDFs in ../../Subs (SRT-style captions exported to
PDF) into clean, continuous-text markdown, one file per episode, plus a
chronological/searchable index. Two series are handled: the main Russian-language
show (files directly in Subs/) and "The Other Russian" (Subs/The Other Russian/).

Requires the `pdftotext` binary (poppler-utils). Pure stdlib otherwise.

Re-run whenever new episode PDFs are added; it rebuilds posts/ and index.tsv
from scratch each time.
"""

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCHIVE_DIR = HERE.parent            # .../Youtube blog/archive
SUBS_DIR = ARCHIVE_DIR.parent / "Subs"
POSTS_DIR = ARCHIVE_DIR / "posts"
INDEX_PATH = ARCHIVE_DIR / "index.tsv"

# filename -> skip reason, files we deliberately do not process
SKIP_FILES = {
    "Archive.zip": "backup zip, contents duplicate already-present loose PDFs",
}

TIMESTAMP_LINE_RE = re.compile(r"^\d{2}:\d{2}:\d{2}[,.]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[,.]\d{3}")
INDEX_LINE_RE = re.compile(r"^\d+$")

# "EP17. Безопасность.pdf", "EP 100. Опасные люди.pdf", "EP01. Бэд трип.pdf",
# "EP07.pdf", "EP102Приходи поговорить.pdf" (missing separator)
FILENAME_EP_RE = re.compile(r"^EP\s?0*(\d+)\.?\s*(.*?)\.pdf$", re.IGNORECASE)
OTHER_RUSSIAN_EP_RE = re.compile(r"^Vlad's podcast\.\s*Episode\s*0*(\d+)\.pdf$", re.IGNORECASE)


def srt_pdf_to_text(pdf_path):
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext failed on {pdf_path}: {result.stderr[:300]}")
    raw = result.stdout

    lines = raw.split("\n")
    kept = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if INDEX_LINE_RE.match(stripped):
            continue
        if TIMESTAMP_LINE_RE.match(stripped):
            continue
        kept.append(stripped)

    # Caption fragments -> flowing text: join fragments with a space, but start
    # a new paragraph after fragments ending in sentence-final punctuation
    # followed by a long gap is not detectable here, so we just join with
    # spaces and let sentence punctuation create natural breaks on read-through.
    text = " ".join(kept)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"([.!?])\s+", r"\1\n\n", text)  # paragraph break after sentences
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def slugify(s, max_len=60):
    s = s.strip().strip(".-_ ")
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s)
    return s[:max_len].strip("-")


def process_series(source_dir, series_slug, series_label, ep_pattern, out_subdir):
    entries = []
    review_notes = []
    seen_ep_numbers = {}

    pdfs = sorted(p for p in source_dir.iterdir() if p.suffix.lower() == ".pdf")
    for pdf in pdfs:
        if pdf.name in SKIP_FILES:
            review_notes.append(f"Skipped {pdf.name}: {SKIP_FILES[pdf.name]}")
            continue

        m = ep_pattern.match(pdf.name)
        if m:
            ep_num = int(m.group(1))
            title = m.group(2).strip(" .-") if m.lastindex and m.lastindex >= 2 else ""
        else:
            ep_num = None
            title = pdf.stem
            review_notes.append(f"Could not parse episode number from filename: {pdf.name}")

        try:
            text = srt_pdf_to_text(pdf)
        except Exception as e:  # noqa: BLE001
            review_notes.append(f"Failed to extract text from {pdf.name}: {e}")
            continue

        word_count = len(text.split())
        if not title:
            flat = re.sub(r"\s+", " ", text).strip()
            snippet = flat[:150].rsplit(" ", 1)[0]
            title = snippet
        title = re.sub(r"\s+", " ", title).strip()

        ep_key = ep_num if ep_num is not None else pdf.stem
        if ep_key in seen_ep_numbers:
            review_notes.append(
                f"Possible duplicate: {pdf.name} and {seen_ep_numbers[ep_key]} both map to episode {ep_key}"
            )
        else:
            seen_ep_numbers[ep_key] = pdf.name

        num_str = f"{ep_num:03d}" if ep_num is not None else "unk"
        slug = slugify(title) or "untitled"
        fname = f"EP{num_str}-{slug}.md"
        out_dir = POSTS_DIR / out_subdir
        out_dir.mkdir(parents=True, exist_ok=True)
        fpath = out_dir / fname

        fm = [
            "---",
            f"id: podcast-{series_slug}-ep{num_str}",
            "type: source",
            "status: archived",
            "canonical: true",
            f"series: \"{series_label}\"",
            f"episode_number: {ep_num if ep_num is not None else 'null'}",
            f"source_file: \"{pdf.relative_to(SUBS_DIR)}\"",
            f"word_count: {word_count}",
            "guest: null",
            "date: null",
            "themes: []",
            "permissions: unconfirmed",
            "---",
        ]
        content = "\n".join(fm) + f"\n\n# {title}\n\n{text}\n"
        fpath.write_text(content, encoding="utf-8")

        entries.append(
            {
                "series": series_label,
                "episode": num_str,
                "title": title,
                "word_count": word_count,
                "file": str(fpath.relative_to(ARCHIVE_DIR)),
                "source_file": pdf.name,
            }
        )

    return entries, review_notes


def main():
    all_entries = []
    all_notes = []

    entries, notes = process_series(
        SUBS_DIR,
        "entheogenic-renaissance",
        "Энтеогенный Ренессанс (main show)",
        FILENAME_EP_RE,
        "entheogenic-renaissance",
    )
    all_entries += entries
    all_notes += notes

    other_dir = SUBS_DIR / "The Other Russian"
    if other_dir.is_dir():
        entries2, notes2 = process_series(
            other_dir,
            "the-other-russian",
            "The Other Russian",
            OTHER_RUSSIAN_EP_RE,
            "the-other-russian",
        )
        all_entries += entries2
        all_notes += notes2

    def sanitize(v):
        return re.sub(r"\s+", " ", str(v)).strip()

    all_entries.sort(key=lambda e: (e["series"], e["episode"]))
    header = "\t".join(["series", "episode", "title", "word_count", "file", "source_file"])
    rows = [
        "\t".join(
            sanitize(v)
            for v in (e["series"], e["episode"], e["title"], e["word_count"], e["file"], e["source_file"])
        )
        for e in all_entries
    ]
    INDEX_PATH.write_text(header + "\n" + "\n".join(rows) + "\n", encoding="utf-8")

    print(f"Wrote {len(all_entries)} episode files under {POSTS_DIR}", file=sys.stderr)
    print(f"Wrote index: {INDEX_PATH}", file=sys.stderr)
    if all_notes:
        print(f"\n{len(all_notes)} items need review:", file=sys.stderr)
        for n in all_notes:
            print("  - " + n, file=sys.stderr)


if __name__ == "__main__":
    main()
