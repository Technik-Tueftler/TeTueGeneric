REQUEST_TIMEOUT = 20
try:
    from ..constants import REQUEST_TIMEOUT
except (ModuleNotFoundError, ImportError) as _:
    pass
