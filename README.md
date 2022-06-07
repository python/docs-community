# Python Documentation Community

[![Documentation Status](https://readthedocs.org/projects/docs-community/badge/?version=latest)](https://docs-community.readthedocs.io/en/latest/?badge=latest)

The Python Editorial Board (née Documentation Working Group) was created and accepted by the **Python Steering Council** in 2021
to help bootstrap a larger documentation team and community.

This repo serves as documentation for the team, community, and the Editorial Board.

For example, to find out more about us and what we do, [read the docs](https://docs-community.readthedocs.io/en/latest/).

## Build docs and view changes

1. Clone this repo

   ```console
   git clone https://github.com/python/docs-community.git
   cd docs-community
   ```

2. Create a new Python virtual environment

   ```console
   python -m venv docs-wg-env
   ```

3. Activate the environment ([platform/shell-specific](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments))

4. Install dependencies

   ```console
   python -m pip install -r requirements.txt
   ```
5. Build the docs, open them in your browser and update whenever changes are made

   ```console
   sphinx-autobuild --open-browser docs docs/_build
   ```

