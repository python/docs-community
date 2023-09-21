# Project information
# ===================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Documentation Community"
author = "Documentation Team"


# General configuration
# =====================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# A list of strings that are module names of Sphinx extensions
extensions = [
    "sphinx_copybutton",
    "myst_parser",
]

# The master toctree document
master_doc = "index"

# Patterns to exclude during source file detetection
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Minimum Sphinx version as a string
needs_sphinx = "4.0"


# Options for HTML output
# =======================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML pages
html_theme = "furo"


# Options for the linkcheck builder
# =================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

# A list of patterns to ignore when checking for broken links
linkcheck_ignore = [
    # RTD preview builds:
    r"https://[a-zA-Z0-9.-]+\.org\.readthedocs\.build/[a-zA-Z0-9.-]+/[a-zA-Z0-9.-]+/",
    # Deleted Plausible page:
    r"https://plausible\.io/share/hugovk-cpython\.readthedocs\.io\?auth=XDF9fK3EB2dEHCr4sC9hn",
    # HackMD anchors:
    r"https://hackmd\.io/[^?]+\?[^#]+#.+"
]
