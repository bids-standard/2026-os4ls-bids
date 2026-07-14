.PHONY: emails pdf clean sync-docs dartmouth-md BIDS.bib

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

# Generic pattern: any foo.docx -> foo.md via docflow.
%.md: %.docx
	$(DOCFLOW) convert docx-to-md $< -o $@

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
