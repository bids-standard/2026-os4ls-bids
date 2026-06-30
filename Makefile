.PHONY: emails

emails:
	rsync -a $$(notmuch search --output files date:1w.. OS4S call bids) emails/cur/
	git annex add emails
	# TODO: make "better" and to do only for freshly staged so we could revert for
	# some we could share
	git annex metadata emails --set distribution-restrictions=might-be-sensitive --force
