#!/usr/bin/env python3
"""
Parse Telegram Desktop HTML export files (messages.html, messages2.html, ...)
for the "Энтеогенный Ренессанс" channel into one markdown file per publication,
plus a chronological TSV index.

Source: ../messages.html, ../messages2.html, ../messages3.html (Telegram Desktop export)
Output: ../posts/<year>/<date>-<id>.md, ../index.tsv

Re-run whenever a fresh export replaces the source files. Pure standard library,
no external dependencies, so it runs anywhere Python 3 runs.
"""

import html
import re
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent.parent  # sources/telegram
OUT_DIR = Path(__file__).resolve().parent.parent          # sources/telegram/archive
POSTS_DIR = OUT_DIR / "posts"
INDEX_PATH = OUT_DIR / "index.tsv"

SOURCE_FILES = ["messages.html", "messages2.html", "messages3.html"]

DIV_OPEN_RE = re.compile(r"<div\b([^>]*)>", re.IGNORECASE)
DIV_CLOSE_RE = re.compile(r"</div\s*>", re.IGNORECASE)
CLASS_RE = re.compile(r'class="([^"]*)"')
ID_RE = re.compile(r'id="message(-?\d+)"')
DATE_TITLE_RE = re.compile(
    r'<div class="pull_right date details" title="([^"]*)"[^>]*>\s*([\d:]+)\s*</div>'
)
FROM_NAME_RE = re.compile(r'<div class="from_name">(.*?)</div>', re.DOTALL)
TEXT_DIV_RE = re.compile(r'<div class="text">(.*?)</div>\s*(?:<span class="reactions"|</div>\s*</div>)', re.DOTALL)
SERVICE_BODY_RE = re.compile(r'<div class="body details">(.*?)</div>', re.DOTALL)
REPLY_TO_RE = re.compile(r'class="reply_to details">.*?#go_to_message(-?\d+)', re.DOTALL)
FORWARDED_NAME_RE = re.compile(
    r'<div class="forwarded body">.*?<div class="from_name">(.*?)</div>', re.DOTALL
)
POLL_QUESTION_RE = re.compile(r'class="media_poll_question">(.*?)<', re.DOTALL)

MEDIA_TYPE_RE = re.compile(r'class="media clearfix pull_left media_(\w+)"')
MEDIA_TYPE_MARKERS = [
    ("round_video", "round_video_filler"),
    ("sticker", 'class="sticker_wrap'),
    ("animation", 'class="animated_wrap'),
    ("poll", "media_poll"),
    ("location", "media_location"),
]


def find_matching_close(text, start_of_open_tag_content_pos, open_tag_end_pos):
    """Given position right after a <div ...> opening tag, find the offset of
    the matching </div>, accounting for nested divs. Returns the offset of the
    matching </div>'s start."""
    depth = 1
    pos = open_tag_end_pos
    while depth > 0:
        next_open = DIV_OPEN_RE.search(text, pos)
        next_close = DIV_CLOSE_RE.search(text, pos)
        if not next_close:
            raise ValueError("unbalanced div, no closing tag found")
        if next_open and next_open.start() < next_close.start():
            depth += 1
            pos = next_open.end()
        else:
            depth -= 1
            pos = next_close.end()
            if depth == 0:
                return next_close.start()
    raise ValueError("unreachable")


def iter_top_level_message_divs(html_text):
    """Yield (block_text, class_attr) for each top-level <div class="message ...">
    block inside the history container."""
    pos = 0
    while True:
        m = re.search(r'<div class="(message[^"]*)"', html_text[pos:])
        if not m:
            return
        abs_start = pos + m.start()
        class_attr = m.group(1)
        open_tag_match = DIV_OPEN_RE.match(html_text, abs_start)
        open_end = open_tag_match.end()
        close_start = find_matching_close(html_text, abs_start, open_end)
        block = html_text[abs_start:close_start]
        yield block, class_attr
        pos = close_start + len("</div>")


def clean_inline_html(fragment):
    if fragment is None:
        return ""
    t = fragment
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.IGNORECASE)
    t = re.sub(r"</p>\s*<p[^>]*>", "\n\n", t, flags=re.IGNORECASE)
    t = re.sub(r"<a\s+href=\"([^\"]*)\"[^>]*>(.*?)</a>", _link_repl, t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<(s|strike|del)>(.*?)</\1>", r"~~\2~~", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<(u)>(.*?)</\1>", r"\2", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<tg-emoji[^>]*>(.*?)</tg-emoji>", r"\1", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<(pre|code)>(.*?)</\1>", r"`\2`", t, flags=re.IGNORECASE | re.DOTALL)
    t = re.sub(r"<[^>]+>", "", t)  # strip anything left
    t = html.unescape(t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def _link_repl(m):
    href, label = m.group(1), m.group(2).strip()
    label_clean = re.sub(r"<[^>]+>", "", label).strip()
    if not href:
        return label_clean
    if not label_clean or label_clean == href:
        return href
    return f"[{label_clean}]({href})"


def detect_media_types(block):
    types = list(dict.fromkeys(MEDIA_TYPE_RE.findall(block)))  # dedupe, keep order
    for name, marker in MEDIA_TYPE_MARKERS:
        if marker in block and name not in types:
            types.append(name)
    if "media_wrap" in block and not types:
        types.append("unknown")
    return types


def parse_date_title(raw_title):
    # "21.09.2023 10:23:49 UTC+01:00" -> ("2023-09-21", "10:23:49")
    m = re.match(r"(\d{2})\.(\d{2})\.(\d{4}) (\d{2}:\d{2}:\d{2})", raw_title)
    if not m:
        return None, None
    dd, mm, yyyy, hms = m.groups()
    return f"{yyyy}-{mm}-{dd}", hms


def parse_message_block(block, class_attr, source_file):
    is_service = "message service" in class_attr
    is_joined = "joined" in class_attr
    id_m = ID_RE.search(block)
    msg_id = id_m.group(1) if id_m else None

    if is_service:
        body_m = SERVICE_BODY_RE.search(block)
        body_text = clean_inline_html(body_m.group(1)) if body_m else ""
        return {
            "id": msg_id,
            "service": True,
            "text": body_text,
            "source_file": source_file,
        }

    date_m = DATE_TITLE_RE.search(block)
    date_iso, time_hms = (None, None)
    date_raw = None
    if date_m:
        date_raw = date_m.group(1)
        date_iso, time_hms = parse_date_title(date_raw)

    from_m = FROM_NAME_RE.search(block)
    from_name = clean_inline_html(from_m.group(1)) if from_m else None

    text_m = TEXT_DIV_RE.search(block)
    text = clean_inline_html(text_m.group(1)) if text_m else ""

    reply_m = REPLY_TO_RE.search(block)
    reply_to = reply_m.group(1) if reply_m else None

    fwd_m = FORWARDED_NAME_RE.search(block)
    forwarded_from = clean_inline_html(fwd_m.group(1)) if fwd_m else None
    if forwarded_from:
        forwarded_from = re.sub(r"\s*\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}\s*$", "", forwarded_from).strip()

    media_types = detect_media_types(block)

    poll_m = POLL_QUESTION_RE.search(block)
    if poll_m and not text:
        text = "[poll] " + clean_inline_html(poll_m.group(1))

    return {
        "id": msg_id,
        "service": False,
        "joined": is_joined,
        "date": date_iso,
        "time": time_hms,
        "datetime_raw": date_raw,
        "from_name": from_name,
        "text": text,
        "reply_to": reply_to,
        "forwarded_from": forwarded_from,
        "media_types": media_types,
        "source_file": source_file,
    }


def slugify_snippet(text, max_len=70):
    first_line = text.strip().split("\n", 1)[0]
    snippet = first_line[:max_len]
    return snippet.replace("\t", " ").strip()


def main():
    errors = []
    publications = []
    current_pub = None
    seen_ids = set()

    for fname in SOURCE_FILES:
        path = SRC_DIR / fname
        html_text = path.read_text(encoding="utf-8")
        count = 0
        for block, class_attr in iter_top_level_message_divs(html_text):
            count += 1
            try:
                parsed = parse_message_block(block, class_attr, fname)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{fname}: parse failure near block #{count}: {e}")
                continue

            if parsed.get("id"):
                if parsed["id"] in seen_ids:
                    errors.append(f"{fname}: duplicate id {parsed['id']}")
                seen_ids.add(parsed["id"])

            if parsed["service"]:
                current_pub = None  # a service message breaks any joined chain
                continue

            if parsed.get("joined") and current_pub is not None:
                if parsed["text"]:
                    current_pub["text"] = (current_pub["text"] + "\n\n" + parsed["text"]).strip()
                current_pub["merged_ids"].append(parsed["id"])
                for mt in parsed["media_types"]:
                    if mt not in current_pub["media_types"]:
                        current_pub["media_types"].append(mt)
                if parsed["forwarded_from"] and not current_pub["forwarded_from"]:
                    current_pub["forwarded_from"] = parsed["forwarded_from"]
                continue

            new_pub = {
                "id": parsed["id"],
                "date": parsed["date"],
                "time": parsed["time"],
                "datetime_raw": parsed["datetime_raw"],
                "from_name": parsed["from_name"],
                "text": parsed["text"],
                "reply_to": parsed["reply_to"],
                "forwarded_from": parsed["forwarded_from"],
                "media_types": list(parsed["media_types"]),
                "merged_ids": [parsed["id"]],
                "source_file": parsed["source_file"],
            }
            publications.append(new_pub)
            current_pub = new_pub

        print(f"{fname}: {count} top-level message divs processed", file=sys.stderr)

    print(f"Total publications after joined-message merge: {len(publications)}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} parse warnings (see stderr detail below)", file=sys.stderr)
        for e in errors[:30]:
            print("  " + e, file=sys.stderr)
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more", file=sys.stderr)

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    index_rows = []

    for pub in publications:
        if not pub["date"] or not pub["id"]:
            errors.append(f"skipped publication missing date/id: {pub.get('id')}")
            continue
        year = pub["date"][:4]
        year_dir = POSTS_DIR / year
        year_dir.mkdir(exist_ok=True)
        fname = f"{pub['date']}-{pub['id']}.md"
        fpath = year_dir / fname

        media_str = ", ".join(pub["media_types"]) if pub["media_types"] else "none"
        merged_str = ",".join(pub["merged_ids"])

        fm_lines = [
            "---",
            f"id: telegram-post-{pub['id']}",
            "type: source",
            "status: archived",
            "canonical: true",
            f"channel: \"Энтеогенный Ренессанс\"",
            f"telegram_message_id: {pub['id']}",
            f"date: {pub['date']}",
            f"time_utc_local: \"{pub['time']}\"",
            f"datetime_raw: \"{pub['datetime_raw']}\"",
            f"media: {media_str}",
        ]
        if pub["forwarded_from"]:
            fm_lines.append(f"forwarded_from: \"{pub['forwarded_from']}\"")
        if pub["reply_to"]:
            fm_lines.append(f"reply_to_message_id: {pub['reply_to']}")
        if len(pub["merged_ids"]) > 1:
            fm_lines.append(f"merged_message_ids: [{merged_str}]")
        fm_lines.append(f"source_file: {pub['source_file']}")
        fm_lines.append("---")

        title = slugify_snippet(pub["text"]) if pub["text"] else f"[{media_str}, no caption]"
        body = pub["text"] if pub["text"] else "*(media only, no caption text)*"

        content = "\n".join(fm_lines) + f"\n\n# {title}\n\n{body}\n"
        fpath.write_text(content, encoding="utf-8")

        index_rows.append(
            "\t".join(
                [
                    pub["date"],
                    pub["time"] or "",
                    pub["id"],
                    media_str,
                    "yes" if pub["forwarded_from"] else "no",
                    str(fpath.relative_to(OUT_DIR)),
                    title.replace("\t", " "),
                ]
            )
        )

    index_rows.sort()  # chronological, since date/time are the leading columns
    header = "\t".join(["date", "time", "id", "media", "forwarded", "file", "title_snippet"])
    INDEX_PATH.write_text(header + "\n" + "\n".join(index_rows) + "\n", encoding="utf-8")

    print(f"Wrote {len(index_rows)} post files under {POSTS_DIR}", file=sys.stderr)
    print(f"Wrote index: {INDEX_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
