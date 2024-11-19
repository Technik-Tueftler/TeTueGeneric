REQUEST_TIMEOUT = 20
LOG_FILE_PATH = "files/henCommander.log"
try:
    from ..constants import REQUEST_TIMEOUT
except (ModuleNotFoundError, ImportError) as _:
    pass
try:
    from ..constants import LOG_FILE_PATH
except (ModuleNotFoundError, ImportError) as _:
    pass