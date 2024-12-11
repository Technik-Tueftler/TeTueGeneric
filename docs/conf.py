# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.insert(0, os.path.abspath("../"))

from src import __version__

project = 'TeTueGeneric'
copyright = '2024, Technik Tueftler'
author = 'Technik Tueftler'
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', # docstrings like google and NumPy
    'sphinx.ext.intersphinx', # for intersphinx_mapping
    'sphinx_copybutton',
    'sphinx_toolbox.more_autodoc.typehints', # use type hints
    'myst_parser', # for Markdown documentation
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
    }

autodoc_member_order = 'bysource'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
