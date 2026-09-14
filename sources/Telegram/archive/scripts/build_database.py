#!/usr/bin/env python3
"""
Build a queryable SQLite database from the parsed Telegram archive posts
(posts/<year>/<date>-<id>.md), plus a pre/post 2025-01-01 voice-drift summary.

Run after parse_archive.py, from anywhere: python3 build_database.py
Source: ../posts/<year>/*.md
Output: ../telegram_archive.db, ../voice-drift-stats.json

Pure standard library, idempotent, safe to re-run whenever the archive
is re-parsed. See ../../../research/telegram-archive-voice-analysis.md
for the analysis this feeds.
"""
import glob
import os
import re
import sqlite3
import json
import collections
import datetime
from pathlib import Path

ARCHIVE_DIR = Path(__file__).resolve().parent.parent  # sources/Telegram/archive
POSTS_DIR = ARCHIVE_DIR / "posts"
DB_PATH = ARCHIVE_DIR / "telegram_archive.db"
STATS_PATH = ARCHIVE_DIR / "voice-drift-stats.json"
SPLIT_DATE = datetime.date(2025, 1, 1)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
HASHTAG_RE = re.compile(r"#[\wА-Яа-яЁё]+")
LINK_RE = re.compile(r"https?://\S+")
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]"
)
WORD_RE = re.compile(r"[А-Яа-яЁёA-Za-z]{2,}")

STOPWORDS = set("""
и в не на что с по для это как я вы он она они мы ты у из за к от до а но или
если то же уже быть был была было были есть нет их его её этого этот эта эти
всё все так там тут где когда только очень просто себя себе свой свою своих
чтобы которые который которая при об про можно нужно надо более менее чем тем
между через без под над после перед во тоже также ещё именно потому поэтому
такой такая такие такое кто чего чему тому им ими ней ним них нём себя мной
тобой нами вами собой да нет ну вот уж ли бы б же ведь мол дескать якобы
""".split())


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw, body = m.groups()
    fm = {}
    for line in fm_raw.split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"')
    return fm, body.strip()


def load_posts():
    files = sorted(glob.glob(str(POSTS_DIR / "*" / "*.md")))
    posts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            fm, body = parse_frontmatter(fh.read())
        posts.append((os.path.relpath(f, ARCHIVE_DIR), fm, body))
    return posts


def analyze(period_label, bodies):
    words, hashtags, openers = collections.Counter(), collections.Counter(), collections.Counter()
    emoji_count = q_marks = exclam = ellipsis = link_count = total_chars = total_words = 0
    n = len(bodies)
    for b in bodies:
        total_chars += len(b)
        hashtags.update(HASHTAG_RE.findall(b))
        link_count += len(LINK_RE.findall(b))
        emoji_count += len(EMOJI_RE.findall(b))
        q_marks += b.count("?")
        exclam += b.count("!")
        ellipsis += b.count("...") + b.count("…")
        ws = WORD_RE.findall(b.lower())
        total_words += len(ws)
        words.update(w for w in ws if w not in STOPWORDS and len(w) > 2)
        first_line = b.strip().split("\n", 1)[0]
        opener = " ".join(first_line.split()[:4])
        if opener:
            openers[opener] += 1
    if n == 0:
        return {"period": period_label, "n_posts": 0}
    return {
        "period": period_label,
        "n_posts": n,
        "avg_chars": round(total_chars / n, 1),
        "avg_words": round(total_words / n, 1),
        "questions_per_post": round(q_marks / n, 2),
        "exclam_per_post": round(exclam / n, 2),
        "ellipsis_per_post": round(ellipsis / n, 2),
        "emoji_per_post": round(emoji_count / n, 2),
        "links_per_post": round(link_count / n, 2),
        "pct_with_hashtags": round(100 * sum(1 for b in bodies if HASHTAG_RE.search(b)) / n, 1),
        "top_words": words.most_common(40),
        "top_hashtags": hashtags.most_common(20),
        "top_openers": [o for o in openers.most_common(15) if o[1] > 1],
    }


def main():
    posts = load_posts()
    print(f"Loaded {len(posts)} posts from {POSTS_DIR}")

    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE posts (
            telegram_message_id INTEGER PRIMARY KEY,
            date TEXT,
            time_utc_local TEXT,
            channel TEXT,
            media TEXT,
            forwarded_from TEXT,
            merged_message_ids TEXT,
            reply_to_id TEXT,
            title TEXT,
            body TEXT,
            word_count INTEGER,
            char_count INTEGER,
            hashtag_count INTEGER,
            link_count INTEGER,
            emoji_count INTEGER,
            period TEXT,
            source_file TEXT
        )
    """)
    cur.execute("CREATE INDEX idx_date ON posts(date)")
    cur.execute("CREATE INDEX idx_period ON posts(period)")

    rows, pre_bodies, post_bodies = [], [], []
    for rel_path, fm, body in posts:
        date = fm.get("date", "")
        try:
            period = "pre-2025" if datetime.date.fromisoformat(date) < SPLIT_DATE else "post-2025"
        except ValueError:
            period = "unknown"
        title = body.split("\n", 1)[0].lstrip("# ").strip() if body else ""
        rows.append((
            int(fm.get("telegram_message_id", 0) or 0),
            date,
            fm.get("time_utc_local", ""),
            fm.get("channel", ""),
            fm.get("media", "none"),
            fm.get("forwarded_from", ""),
            fm.get("merged_message_ids", ""),
            fm.get("reply_to_id", ""),
            title,
            body,
            len(WORD_RE.findall(body)),
            len(body),
            len(HASHTAG_RE.findall(body)),
            len(LINK_RE.findall(body)),
            len(EMOJI_RE.findall(body)),
            period,
            rel_path,
        ))
        (pre_bodies if period == "pre-2025" else post_bodies if period == "post-2025" else []).append(body)

    cur.executemany("INSERT INTO posts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    conn.commit()
    conn.close()
    print(f"Wrote {DB_PATH}")

    stats = {
        "pre_2025": analyze(f"pre-2025 (2023-09-21 to {SPLIT_DATE.isoformat()})", pre_bodies),
        "post_2025": analyze(f"post-2025 ({SPLIT_DATE.isoformat()} onward)", post_bodies),
    }
    with open(STATS_PATH, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"Wrote {STATS_PATH}")


if __name__ == "__main__":
    main()
