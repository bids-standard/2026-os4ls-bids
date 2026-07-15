.PHONY: emails pdf clean sync-docs dartmouth-md

# Absolute path to the directory of this Makefile. Lets rules reference
# scripts/, subs/, BIDS.bib etc. by an absolute path so `make -f ../Makefile`
# (or any other subdir invocation) still finds them.
TOPDIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

# Requires: pandoc + a TeX distribution providing xelatex
#   (Debian/Ubuntu: apt install pandoc texlive-xetex texlive-fonts-recommended)
PANDOC ?= pandoc
PANDOC_PDF_OPTS = \
	--pdf-engine=xelatex \
	-V geometry:margin=1in \
	-V fontsize=11pt \
	-V linestretch=1.15 \
	-V colorlinks=true \
	-V linkcolor=NavyBlue \
	-V urlcolor=NavyBlue

pdf: LOI.pdf

%.pdf: %.md
	$(PANDOC) $< -o $@ $(PANDOC_PDF_OPTS)

# Explicit rule for the bios PDF: adds pandoc citeproc against
# Vancouver CSL, 1cm margins, and a small-font override for the
# auto-generated References section so bios + refs fit inside the OS4LS
# Optional Upload's 4-page cap.  Do not adding BIDS.bib since we do not need to refetch
subs/biographies.pdf: subs/biographies.md subs/vancouver.csl subs/refs-header.tex
	$(PANDOC) $< -o $@ \
		--pdf-engine=xelatex \
		-V geometry:margin=1cm \
		-V fontsize=11pt \
		-V linestretch=1.1 \
		-V colorlinks=true \
		-V linkcolor=NavyBlue \
		-V urlcolor=NavyBlue \
		--citeproc \
		--bibliography=BIDS.bib \
		--csl=subs/vancouver.csl \
		--include-in-header=subs/refs-header.tex

clean:
	rm -f LOI.pdf

# Sync shared project documents from Google Drive and convert every .xlsx to .tsv
# via docflow (https://github.com/con/docflow).
# Requires: rclone (with a "gdrive" remote), docflow.
GDRIVE_REMOTE ?= gdrive:BIDS/2026-OS4S-BIDS/
GDRIVE_LOCAL  ?= gdrive

sync-docs:
	rclone sync $(GDRIVE_REMOTE) $(GDRIVE_LOCAL)/
	for f in $(GDRIVE_LOCAL)/*.xlsx; do \
		[ -e "$$f" ] || continue; \
		$(DOCFLOW) convert xlsx-to-tsv "$$f" -o "$${f%.xlsx}.tsv"; \
	done

# Convert .docx to Markdown via docflow (https://github.com/…/docflow).
# Override DOCFLOW to point at the CLI, e.g.:
#   make dartmouth-md DOCFLOW=/home/you/proj/docflow/.venv/bin/docflow
DOCFLOW ?= docflow

# .docx -> .md pipeline. Docflow's docx-to-md uses pandoc's default
# `--wrap=auto`, which reshuffles line-wrapping across pandoc releases
# and dominates diffs between successive Word-round-trip conversions.
# We work around this by post-processing to sentence-per-line: run
# docflow, then unescape pandoc-3.x escapes (\<, \>, \*), then rewrap
# via scripts/sentence-per-line.py. Result: diffs between v_N and
# v_N+1 show only real content changes.
# Set RAW=1 to skip the post-processing (get docflow's raw output).
RAW ?=
%.md: %.docx
	$(DOCFLOW) convert docx-to-md $< -o $@
ifndef RAW
	sed -i 's|\\<|<|g; s|\\>|>|g; s|\\\*|*|g' $@
	python3 $(TOPDIR)scripts/sentence-per-line.py --in-place $@
endif

%.docx_: %.md
	$(DOCFLOW) convert md-to-docx $< -o $@


DARTMOUTH_DOCX := $(wildcard dartmouth/*.docx)
DARTMOUTH_MD   := $(DARTMOUTH_DOCX:.docx=.md)

dartmouth-md: $(DARTMOUTH_MD)

# Sync the shared BIDS Zotero library into a local BIDS.bib.
# Uses scripts/zotero-export-bib.py, which talks to the Zotero Web API
# directly. (docflow's CLI yet to be tuned up for seamless use)
#
# Setup:
#   1. Create a Zotero API key: https://www.zotero.org/settings/keys
#      export ZOTERO_API_KEY=...
#   2. ZOTERO_GROUP_ID is pinned below to the OS4LS BIDS 2.0+ group.
#   3. Leave ZOTERO_COLLECTION empty for the whole group, or set it to
#      an 8-char collection key (find in Zotero web URL:
#      https://www.zotero.org/groups/{GROUP}/collections/{COLLECTION_KEY}).
#
# BIDS.bib is tracked in git; `make BIDS.bib` will say "up to date" if the
# file already exists. Force a refresh with `make -B BIDS.bib` (or
# `rm BIDS.bib && make BIDS.bib`).
ZOTERO_GROUP_ID   ?= 5111637
ZOTERO_COLLECTION ?=

BIDS.bib:
	@[ -n "$$ZOTERO_API_KEY" ] || { \
	  echo "ZOTERO_API_KEY not set — get one at https://www.zotero.org/settings/keys and 'export ZOTERO_API_KEY=...'"; \
	  exit 1; }
	@[ -n "$(ZOTERO_GROUP_ID)" ] || { \
	  echo "Set ZOTERO_GROUP_ID (see 'make BIDS.bib' comment in the Makefile)"; \
	  exit 1; }
	python3 scripts/zotero-export-bib.py \
	  --group $(ZOTERO_GROUP_ID) \
	  $(if $(ZOTERO_COLLECTION),--collection $(ZOTERO_COLLECTION),) \
	  --output $@

emails:
	rsync -a $$(notmuch search --output files date:1w.. OS4S call bids) emails/cur/
	git annex add emails
	# TODO: make "better" and to do only for freshly staged so we could revert for
	# some we could share
	git annex metadata emails --set distribution-restrictions=might-be-sensitive --force
