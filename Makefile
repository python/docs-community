# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON        = python3
VENVDIR       = ./.venv
SPHINXBUILD   = $(VENVDIR)/bin/sphinx-build
SPHINXOPTS    = --fail-on-warning --keep-going
BUILDDIR      = _build
BUILDER       = html
JOBS          = auto
SPHINXLINT    = $(VENVDIR)/bin/sphinx-lint

# Internal variables.
ALLSPHINXOPTS   = --builder $(BUILDER) \
                  --doctree-dir $(BUILDDIR)/doctrees \
                  --jobs $(JOBS) \
                  $(SPHINXOPTS) \
                  docs $(BUILDDIR)/$(BUILDER)

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to create a venv with necessary tools"
	@echo "  html       to make standalone HTML files"
	@echo "  htmlview   to open the index page built by the html target in your browser"
	@echo "  htmllive   to rebuild and reload HTML files in your browser"
	@echo "  clean      to remove the venv and build files"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  lint       to lint all the files"

.PHONY: clean
clean: clean-venv
	-rm -rf $(BUILDDIR)/*

.PHONY: clean-venv
clean-venv:
	rm -rf $(VENVDIR)

.PHONY: venv
venv:
	@if [ -d $(VENVDIR) ] ; then \
		echo "venv already exists."; \
		echo "To recreate it, remove it first with \`make clean-venv'."; \
	else \
		$(MAKE) ensure-venv; \
	fi

.PHONY: ensure-venv
ensure-venv:
	@if [ ! -d $(VENVDIR) ] ; then \
		echo "Creating venv in $(VENVDIR)"; \
		if uv --version > /dev/null; then \
			uv venv --python=$(PYTHON) $(VENVDIR); \
			VIRTUAL_ENV=$(VENVDIR) uv pip install -r requirements.txt; \
		else \
			$(PYTHON) -m venv $(VENVDIR); \
			$(VENVDIR)/bin/python3 -m pip install --upgrade pip; \
			$(VENVDIR)/bin/python3 -m pip install -r requirements.txt; \
		fi; \
		echo "The venv has been created in the $(VENVDIR) directory"; \
	fi

.PHONY: html
html: ensure-venv
	$(SPHINXBUILD) $(ALLSPHINXOPTS)

.PHONY: linkcheck
linkcheck: BUILDER = linkcheck
linkcheck: html
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/$(BUILDER)/output.txt."

.PHONY: htmlview
htmlview: html
	$(PYTHON) -c "import os, webbrowser; webbrowser.open('file://' + os.path.realpath('_build/html/index.html'))"

.PHONY: htmllive
htmllive: SPHINXBUILD = $(VENVDIR)/bin/sphinx-autobuild
# Arbitrarily selected ephemeral port between 49152–65535
# to avoid conflicts with other processes:
htmllive: SPHINXOPTS = --re-ignore="/\.idea/|/venv/" --open-browser --delay 0 --port 55303
htmllive: html

.PHONY: lint
lint: venv
	if uv --version > /dev/null; then \
		$(VENVDIR)/bin/python3 -m pre_commit --version > /dev/null || VIRTUAL_ENV=$(VENVDIR) uv pip install pre-commit; \
	else \
		$(VENVDIR)/bin/python3 -m pre_commit --version > /dev/null || $(VENVDIR)/bin/python3 -m pip install pre-commit; \
	fi;
	$(VENVDIR)/bin/python3 -m pre_commit run --all-files
