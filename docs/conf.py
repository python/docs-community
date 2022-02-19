needs_sphinx = '4.0'

# Sphinx extensions
extensions = [
    'myst_parser',
    'sphinx_copybutton',
]

# The suffix(es) of source filenames.
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Documentation Community'
copyright = '2021, Python'
author = 'Documentation Team'

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML pages.
html_theme = 'furo'

# relative paths to custom static files
html_static_path = ['_static']

