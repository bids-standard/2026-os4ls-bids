.PHONY: emails

emails:
	rsync -a $$(notmuch search --output files date:1w.. OS4S call bids) emails/cur/
