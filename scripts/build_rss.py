#!/usr/bin/env python3
from datetime import datetime, timedelta, timezone
import os, calendar, hashlib

OUT_PATH = "rss/index.xml"
BASE_URL = "https://en.wikipedia.org/wiki/Portal:Current_events"

# Compute two days ago in UTC
target = (datetime.now(timezone.utc) - timedelta(days=2)).replace(hour=0, minute=0)
slug = f"{target.year}_{calendar.month_name[target.month]}_{target.day}"
page_url = f"{BASE_URL}/{slug}"

# RSS metadata
title = f"Wikipedia Current Events for {target.strftime('%Y-%m-%d')}"
pub_date = target.strftime("%a, %d %b %Y %H:%M:%S GMT")
guid = hashlib.sha1(page_url.encode()).hexdigest()

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Wikipedia Current Events (2 days ago, UTC)</title>
<link>https://github.com/CodebergIsBetter/Wikipedia_Current_Events/tree/main</link>
<description>Daily RSS linking to Wikipedia Current Events page from two days prior (UTC).</description>
<lastBuildDate>{datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}</lastBuildDate>
<pubDate>{pub_date}</pubDate>
<generator>Python</generator>
<item>
<title>{title}</title>
<link>{page_url}</link>
<guid isPermaLink="false">{guid}</guid>
<pubDate>{pub_date}</pubDate>
<description>Link to Wikipedia Current Events page for {target.strftime('%Y-%m-%d')} (UTC)</description>
</item>
</channel>
</rss>
"""

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(rss)

print(f"[ok] RSS feed created at {OUT_PATH} → {page_url}")

