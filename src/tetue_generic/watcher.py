"""All functions and features for logging the app
"""

from loguru import logger
from pydantic import BaseModel, FilePath


class WatcherConfiguration(BaseModel):
    """
    Configuration settings for generic_requests
    """

    log_level: str = ""
    log_file_path: FilePath = None


watcher_settings = WatcherConfiguration()


def init_generic_watcher(log_file_path: FilePath) -> None:
    """
    Locale initialization for the transfer of default values 
    for the generic watcher functions 

    Args:
        log_file_path (FilePath): Existing path with file
    """
    watcher_settings.log_file_path = log_file_path


def init_logging(log_level: str) -> None:
    """Initialization of logging to create log file and set level at beginning of the app.

    Args:
        log_level (str): Configured log level
    """
    logger.add(watcher_settings.log_file_path, rotation="500 MB", level=log_level)
