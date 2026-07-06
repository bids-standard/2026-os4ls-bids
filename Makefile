.PHONY: emails pdf clean

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

emails:
	rsync -a $$(notmuch search --output files date:1w.. OS4S call bids) emails/cur/
	git annex add emails
	# TODO: make "better" and to do only for freshly staged so we could revert for
	# some we could share
	git annex metadata emails --set distribution-restrictions=might-be-sensitive --force
