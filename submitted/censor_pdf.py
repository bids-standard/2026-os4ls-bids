#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4", "reportlab>=4"]
# ///
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.63 / Claude Opus 4.7
"""Replace given 1-indexed pages of a PDF with a "SENSORED" placeholder page."""

from __future__ import annotations

import io
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


def make_sensored_page(width: float, height: float) -> PdfReader:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(width, height))
    c.setFont("Helvetica-Bold", min(width, height) / 6)
    c.setFillGray(0.4)
    c.drawCentredString(width / 2, height / 2, "SENSORED")
    c.showPage()
    c.save()
    buf.seek(0)
    return PdfReader(buf)


def main(src: str, dst: str, pages_1indexed: list[int]) -> None:
    reader = PdfReader(src)
    writer = PdfWriter()
    censor = set(pages_1indexed)
    for i, page in enumerate(reader.pages, start=1):
        if i in censor:
            w = float(page.mediabox.width)
            h = float(page.mediabox.height)
            writer.add_page(make_sensored_page(w, h).pages[0])
        else:
            writer.add_page(page)
    with open(dst, "wb") as fh:
        writer.write(fh)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("usage: censor_pdf.py SRC.pdf DST.pdf PAGE [PAGE...]")
    main(sys.argv[1], sys.argv[2], [int(p) for p in sys.argv[3:]])
