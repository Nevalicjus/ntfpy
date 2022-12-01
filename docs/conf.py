# Sphinx Doc Builder Config
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

sys.path.insert(0, os.path.abspath("../src/"))
sys.path.append(os.path.abspath("extensions"))

# Project Info
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ntfpy"
copyright = "2022, Nevalicjus"
author = "Nevalicjus"
release = "0.0.10"

# General
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "resourcelinks"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
locale_dirs = ["locale/"]

# HTML Options
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "domdf_sphinx_theme"
html_static_path = ["_static"]

html_show_sphinx = False
html_logo = "./images/ntfpy-50x50.png"
html_favicon = "./images/ntfpy.ico"

htmlhelp_basename = "ntfpydoc"

# Extension Options

resource_links = {
  "discord": "https://n3v.xyz/support",
  "issues": "https://github.com/nevalicjus/ntfpy/issues",
  "examples": "https://github.com/nevalicjus/ntfpy/tree/main/examples"
}

intersphinx_mapping = {
  "py": ("https://docs.python.org/3", None),
  "req": ("https://requests.readthedocs.io/en/latest/", None)
}

autodoc_default_options = {
    "member-order": "bysource",
    "undoc-members": True,
    "exclude-members": "__weakref__,__dict__,__str__,__module__,__annotations__",
    "autosummary": True
}

napoleon_use_ivar = True
