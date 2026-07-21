# Pages to censor (1-indexed) when producing %_sensored.pdf
CENSOR_PAGES ?= 16 17

.PHONY: all sensored clean
all: sensored

# Build FOO_sensored.pdf for every FOO.pdf in the directory.
# Uses a shell loop so filenames with spaces work (Make's $(wildcard) doesn't).
sensored:
	@set -e; for src in *.pdf; do \
		case "$$src" in *_sensored.pdf) continue;; esac; \
		dst="$${src%.pdf}_sensored.pdf"; \
		if [ ! -e "$$dst" ] || [ "$$src" -nt "$$dst" ] || [ censor_pdf.py -nt "$$dst" ]; then \
			echo "  CENSOR  $$dst"; \
			./censor_pdf.py "$$src" "$$dst" $(CENSOR_PAGES); \
		fi; \
	done

# Direct pattern rule (fine for filenames without spaces).
%_sensored.pdf: %.pdf censor_pdf.py
	./censor_pdf.py "$<" "$@" $(CENSOR_PAGES)

clean:
	@for f in *_sensored.pdf; do [ -e "$$f" ] && rm -f "$$f" && echo "  RM      $$f" || true; done
