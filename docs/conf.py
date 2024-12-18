# pylint: skip-file
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
    'sphinx.ext.viewcode', # open code 
    'sphinx_copybutton', # add copy button in code view
    'sphinx_toolbox.more_autodoc.typehints', # use type hints
    'myst_parser', # for Markdown documentation
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'loguru': ('https://loguru.readthedocs.io/en/stable/', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
    }

autodoc_member_order = 'bysource'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
