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
    "sphinx.ext.intersphinx",
    "myst_parser",
]

# The master toctree document
master_doc = "index"

# Patterns to exclude during source file detection
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "include/minutes-template.md",
]

# Minimum Sphinx version as a string
needs_sphinx = "4.0"

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "devguide": ("https://devguide.python.org/", None),
    "pep": ("https://peps.python.org/", None),
}
intersphinx_disabled_reftypes = []

# Options for HTML output
# =======================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML pages
html_theme = "furo"

html_title = "Python Docs Community Group"

# Options for the linkcheck builder
# =================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

# A list of patterns to ignore when checking for broken links
linkcheck_ignore = [
    # The crawler gets "Anchor not found"
    r"https://github.com.+?#.*",
    r"https://hackmd\.io/[^?]+\?[^#]+#.+",
    # Google Meet gives 404
    r"https://meet.google.com/.*",
    # RTD preview builds:
    r"https://[a-zA-Z0-9.-]+\.org\.readthedocs\.build/[a-zA-Z0-9.-]+/[a-zA-Z0-9.-]+/",
    # Deleted pages:
    r"https://plausible\.io/share/hugovk-cpython\.readthedocs\.io\?auth=XDF9fK3EB2dEHCr4sC9hn",
    r"https://plausible.io/docs.python.org",
    r"https://plausible.io/packaging.python.org",
    r"https://us.pycon.org/2024/registration/category/4",
]
