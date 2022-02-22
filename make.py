#!/usr/bin/env python3
"""Build script for Sphinx documentation.

USAGE:
======

python make.py
    run Sphinx with the html builder

python make.py [builder]
    run Sphinx with the given builder

python make.py [builder] [options...]
    run Sphinx with the given builder and pass all remaining arguments to Sphinx

Output is always in the ``build/`` directory.

"""

import sys

from sphinx.cmd.make_mode import run_make_mode

if __name__ == "__main__":
    argv = sys.argv[1:]
    if not argv:
        raise SystemExit(run_make_mode(["html", "docs", "build"]))
    if len(argv) == 1:
        raise SystemExit(run_make_mode([argv[0], "docs", "build"]))
    raise SystemExit(run_make_mode([argv[0], "docs", "build", *argv[1:]]))
