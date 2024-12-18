"""
This module initializes the package and provides central variables and configurations.
- Defines generic standard variables that can be used throughout the package.
- Imports variables from the parent module if they are already defined to avoid redundancy.
- Enables centralized management and reusability of shared resources.

Note:
- Parent variables are only imported if they are explicitly defined in the parent module.
- Variables from higher-level take precedence.
"""

REQUEST_TIMEOUT = 20
LOG_FILE_PATH = "files/app.log"
try:
    from ..constants import REQUEST_TIMEOUT
except (ModuleNotFoundError, ImportError) as _:
    pass
try:
    from ..constants import LOG_FILE_PATH
except (ModuleNotFoundError, ImportError) as _:
    pass
