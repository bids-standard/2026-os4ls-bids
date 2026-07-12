.PHONY: emails pdf clean sync-docs dartmouth-md

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

# Sync shared project documents from Google Drive and convert every .xlsx to .tsv.
# Requires: rclone (with a "gdrive" remote), csvkit (in2csv, csvformat).
GDRIVE_REMOTE ?= gdrive:BIDS/2026-OS4S-BIDS/
GDRIVE_LOCAL  ?= gdrive

sync-docs:
	rclone sync $(GDRIVE_REMOTE) $(GDRIVE_LOCAL)/
	for f in $(GDRIVE_LOCAL)/*.xlsx; do \
		[ -e "$$f" ] || continue; \
		in2csv "$$f" | csvformat -T > "$${f%.xlsx}.tsv"; \
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

emails:
	rsync -a $$(notmuch search --output files date:1w.. OS4S call bids) emails/cur/
	git annex add emails
	# TODO: make "better" and to do only for freshly staged so we could revert for
	# some we could share
	git annex metadata emails --set distribution-restrictions=might-be-sensitive --force
