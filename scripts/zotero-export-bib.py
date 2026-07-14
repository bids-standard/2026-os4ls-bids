#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.207 / Claude Opus 4.7
"""Export a Zotero group (or a specific collection within it) as BibTeX.

Talks directly to the Zotero Web API. Used because docflow's
`ZoteroClient.export_bibtex()` requires a collection key, but for
group-wide export there is no such key — the group's top level is
addressed as `/groups/{id}/items` with no collection segment.

Paginates via the `Total-Results` header (Zotero caps `format=bibtex`
responses at 100 items per request).
"""

from __future__ import annotations

import argparse
import os
import sys
import urllib.request
from pathlib import Path


def fetch_bibtex(group: str, collection: str | None, api_key: str) -> str:
    base = f"https://api.zotero.org/groups/{group}"
    path = f"/collections/{collection}/items" if collection else "/items"
    chunks: list[str] = []
    start = 0
    while True:
        url = f"{base}{path}?format=bibtex&limit=100&start={start}"
        req = urllib.request.Request(url, headers={"Zotero-API-Key": api_key})
        with urllib.request.urlopen(req) as r:
            text = r.read().decode("utf-8")
            total = int(r.headers.get("Total-Results", "0"))
        if text.strip():
            chunks.append(text)
        start += 100
        if start >= total:
            break
    return "\n".join(chunks)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--group", required=True, help="Zotero group ID")
    p.add_argument(
        "--collection",
        default="",
        help="Optional collection key (omit for the entire group library)",
    )
    p.add_argument("--output", "-o", help="Output path (default: stdout)")
    args = p.parse_args()

    api_key = os.environ.get("ZOTERO_API_KEY")
    if not api_key:
        print("ZOTERO_API_KEY environment variable not set", file=sys.stderr)
        return 1

    bib = fetch_bibtex(args.group, args.collection or None, api_key)

    if args.output:
        Path(args.output).write_text(bib)
        print(
            f"Wrote {args.output} ({bib.count('@')} entries)",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(bib)
    return 0


if __name__ == "__main__":
    sys.exit(main())
