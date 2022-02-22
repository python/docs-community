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
