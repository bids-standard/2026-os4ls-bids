#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.207 / Claude Opus 4.7
"""Sentence-per-line markdown reformatter.

Turns prose paragraphs into "one sentence per line" and joins wrapped
list items into one item per line, while preserving:

- YAML front matter (between `---` fences at the top of the file)
- HTML comments (`<!-- ... -->`, possibly multi-line)
- Fenced code blocks (``` ``` ```` and ``` ~~~ ```)
- ATX headings (`# ...`) and setext-underlined headings
- Pipe tables (`| col | col |`)
- Pandoc simple / multi-line tables (rows separated by `--- --- ---`
  lines)
- Pandoc grid tables (`+---+---+`)
- Blockquote structure (`>` prefix preserved; inner prose sentence-split)

Sentence splitting uses `\\.\\s+(?=[A-Z\\[])` with abbreviation
protection for `Ph.D.`, `Dr.`, `Prof.`, `Mr.`, `Mrs.`, `Ms.`, `St.`,
`Jr.`, `Sr.`, `e.g.`, `i.e.`, `et al.`, `U.S.`, `U.K.`, `U.C.`

Numbered-list items are recognized as `N.` or `N.M ` markers only when
they appear as the FIRST content line of a paragraph. This prevents
mid-paragraph tokens like "BIDS 2.0" from being misclassified as list
items.

Designed to be lifted verbatim into a Python module (e.g. `docflow`);
stdlib only.

Usage:
    python3 sentence-per-line.py input.md [-o output.md]
    # or in-place:
    python3 sentence-per-line.py --in-place input.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ABBREVIATIONS = [
    "Ph.D.", "Ph.D",
    "Dr.", "Prof.", "Mr.", "Mrs.", "Ms.", "St.",
    "Jr.", "Sr.",
    "e.g.", "i.e.", "et al.",
    "U.S.", "U.K.", "U.C.",
    "Fig.", "Eq.", "No.", "vs.", "cf.",
]
_ABBR_NULL = "\x00"

_NUM_LIST_RE = re.compile(r"^\d+(?:\.\d+)*[\.\)]?\s")
_DASH_LIST_RE = re.compile(r"^[-*+]\s")
_TABLE_SEP_RE = re.compile(r"^\s*-{3,}(\s+-{3,})+\s*$")
_GRID_TABLE_RE = re.compile(r"^\+[-=+]+\+")
# Long horizontal rule — opens/closes pandoc multi-line tables. Require
# 20+ dashes to avoid matching short markdown-<hr> or YAML `---` markers.
_HR_LONG_RE = re.compile(r"^\s*-{20,}\s*$")
_ATX_HEADING_RE = re.compile(r"^#{1,6}\s")
_SETEXT_UNDERLINE_RE = re.compile(r"^(={3,}|-{3,})\s*$")


_INITIAL_RE = re.compile(r"(^|\s)([A-Z])\.(\s+[A-Z][a-z])")


def _protect_abbrev(text: str) -> str:
    for a in ABBREVIATIONS:
        text = text.replace(a, a.replace(".", _ABBR_NULL))
    # Protect single-letter mid-name initials like "Yaroslav O. Halchenko"
    # (capital letter, period, whitespace, capitalised-first-word). Requires
    # whitespace/start-of-string BEFORE the initial so that "PhD. He was..."
    # (D preceded by h, no whitespace) still splits as end-of-sentence.
    text = _INITIAL_RE.sub(lambda m: m.group(1) + m.group(2) + _ABBR_NULL + m.group(3), text)
    return text


def _restore_abbrev(text: str) -> str:
    return text.replace(_ABBR_NULL, ".")


def sentence_split(paragraph: str) -> list[str]:
    """Split a single-string paragraph into sentences.

    Splits at `. ` (period-plus-whitespace) followed by a capital letter
    or an opening bracket `[` (pandoc citation / span syntax).
    """
    protected = _protect_abbrev(paragraph)
    parts = re.split(r"\.\s+(?=[A-Z\[])", protected)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            part = part + "."
        out.append(_restore_abbrev(part))
    return out


def _first_content(lines: list[str]) -> str:
    for ln in lines:
        s = ln.strip()
        if s:
            return s
    return ""


def _looks_like_table(lines: list[str]) -> bool:
    for ln in lines:
        s = ln.strip()
        if s.startswith("|") or _TABLE_SEP_RE.match(ln) or _GRID_TABLE_RE.match(s):
            return True
    return False


def _looks_like_table_opener(line: str) -> bool:
    """First line of a table block (pipe / grid / simple / multi-line)."""
    s = line.strip()
    return (
        s.startswith("|")
        or s.startswith("+--")
        or bool(_HR_LONG_RE.match(line))
        or bool(_TABLE_SEP_RE.match(line))
    )


def _consume_table(lines: list[str], start: int) -> int:
    """Return the index just past the last line of the table starting at `start`.

    Pandoc emits four table flavours from docx:
      - pipe: rows start with `|`; ends at first non-pipe line
      - grid: rows bracketed by `+---+`; ends at first blank line
      - multi-line: opens with a long HR (20+ dashes), rows separated by
        blank lines, closes with another long HR
      - simple: `header row` + `--- --- ---` separator + body; ends at blank
    """
    n = len(lines)
    first = lines[start]
    first_s = first.strip()

    if first_s.startswith("|"):
        i = start + 1
        while i < n and lines[i].strip().startswith("|"):
            i += 1
        return i
    if first_s.startswith("+"):
        i = start + 1
        while i < n and lines[i].strip():
            i += 1
        return i
    if _HR_LONG_RE.match(first):
        i = start + 1
        while i < n:
            if _HR_LONG_RE.match(lines[i]):
                return i + 1
            i += 1
        return i
    if _TABLE_SEP_RE.match(first):
        i = start + 1
        while i < n and lines[i].strip():
            i += 1
        return i
    return start + 1


def _looks_like_setext_heading(lines: list[str]) -> bool:
    return len(lines) == 2 and bool(_SETEXT_UNDERLINE_RE.match(lines[1].strip()))


def _is_blockquote(lines: list[str]) -> bool:
    return bool(_first_content(lines).startswith(">"))


def _join_list_items(lines: list[str], marker_re: re.Pattern[str]) -> list[str]:
    """Turn a list block (possibly wrapped items) into one item per line.

    Any non-empty line that starts with the marker begins a new item;
    other non-empty lines are continuations and get joined into the
    previous item's line.
    """
    items: list[str] = []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if marker_re.match(s) or not items:
            items.append(s)
        else:
            items[-1] += " " + s
    return items


def _process_blockquote(lines: list[str]) -> str:
    stripped = []
    for ln in lines:
        s = ln
        # remove leading "> " (or ">" alone)
        m = re.match(r"^\s*>\s?(.*)$", s)
        stripped.append(m.group(1) if m else s)
    inner_md = "\n".join(stripped)
    inner_out = reformat_paragraphs(inner_md)
    return "\n".join("> " + l if l else ">" for l in inner_out.splitlines())


def _process_content_paragraph(lines: list[str]) -> str:
    first = _first_content(lines)

    # Tables (pipe / simple / multi-line / grid) — preserve as-is.
    if _looks_like_table(lines):
        return "\n".join(lines)

    # Setext heading (two lines: title + === or ---) — preserve.
    if _looks_like_setext_heading(lines):
        return "\n".join(lines)

    # ATX heading — preserve (single line).
    if _ATX_HEADING_RE.match(first):
        return "\n".join(lines)

    # Blockquote — recurse into stripped content.
    if _is_blockquote(lines):
        return _process_blockquote(lines)

    # Numbered list — recognize only when the FIRST content line starts
    # with the numbered marker. This avoids "in-person BIDS\n2.0 release
    # event" being misread as a numbered list.
    if _NUM_LIST_RE.match(first):
        items = _join_list_items(lines, _NUM_LIST_RE)
        return "\n".join(items)

    # Dash/bullet list.
    if _DASH_LIST_RE.match(first):
        items = _join_list_items(lines, _DASH_LIST_RE)
        return "\n".join(items)

    # Prose paragraph.
    joined = " ".join(l.strip() for l in lines if l.strip())
    return "\n".join(sentence_split(joined))


def reformat_paragraphs(md: str) -> str:
    """Main entry point — transform full markdown text."""
    lines = md.splitlines()
    n = len(lines)
    out: list[str] = []
    i = 0

    # Preamble: skip blank lines and HTML comments so YAML front-matter
    # can be recognised even when it appears after a top-of-file
    # HTML comment (a common pandoc pattern).
    while i < n:
        line = lines[i]
        if not line.strip():
            out.append(line)
            i += 1
            continue
        if line.lstrip().startswith("<!--"):
            j = i
            while j < n and "-->" not in lines[j]:
                j += 1
            out.extend(lines[i:j + 1])
            i = j + 1
            continue
        break

    # YAML front matter, right after any preamble.
    if i < n and lines[i].strip() == "---":
        j = i + 1
        while j < n and lines[j].strip() != "---":
            j += 1
        if j < n:  # closing --- found
            out.extend(lines[i:j + 1])
            i = j + 1

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Blank line separator.
        if not stripped:
            out.append(line)
            i += 1
            continue

        # HTML comment (possibly multi-line).
        if "<!--" in stripped:
            j = i
            while j < n and "-->" not in lines[j]:
                j += 1
            out.extend(lines[i:j + 1])
            i = j + 1
            continue

        # Fenced code block.
        fence_match = re.match(r"^(\s*)(```+|~~~+)", line)
        if fence_match:
            fence = fence_match.group(2)
            out.append(line)
            j = i + 1
            while j < n and not re.match(rf"^\s*{re.escape(fence)}", lines[j]):
                out.append(lines[j])
                j += 1
            if j < n:
                out.append(lines[j])
                j += 1
            i = j
            continue

        # Table (may span multiple blank-line-separated row groups, so
        # detect BEFORE the ordinary paragraph collector).
        if _looks_like_table_opener(line):
            end = _consume_table(lines, i)
            out.extend(lines[i:end])
            i = end
            continue

        # Collect a paragraph (contiguous non-blank lines).
        j = i
        while j < n and lines[j].strip():
            j += 1
        paragraph_lines = lines[i:j]
        out.append(_process_content_paragraph(paragraph_lines))
        i = j

    return "\n".join(out) + ("\n" if md.endswith("\n") else "")


def _cli() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="Markdown file to reformat")
    p.add_argument("-o", "--output", type=Path, help="Output path (default: stdout)")
    p.add_argument("--in-place", action="store_true", help="Rewrite the input file")
    args = p.parse_args()

    src = args.input.read_text(encoding="utf-8")
    out = reformat_paragraphs(src)

    if args.in_place:
        args.input.write_text(out, encoding="utf-8")
        print(f"Reformatted {args.input}", file=sys.stderr)
    elif args.output:
        args.output.write_text(out, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
