"""
This module initializes the main application and provides central functions, 
classes and configurations. It serves as the entry point for the entire application 
and enables
- The loading of global configurations and resources.
- The initialization of submodules and packages.
- The import and provision of frequently used functions and constants.
"""
from .configuration import *
from .tetue_generic.generic_requests import *
from .tetue_generic.watcher import *

__version__ = "v0.2.0"
__repository__ = "https://github.com/Technik-Tueftler/TeTueGeneric"
