# Makefile, redirecting to "make.py"

# Sphinx options, can be set from the command line
OPTS =

# This runs for `make` without any arguments
all:
	python3 make.py

html:
	python3 make.py html $(OPTS)

check-links:
	python3 make.py linkcheck $(OPTS)
