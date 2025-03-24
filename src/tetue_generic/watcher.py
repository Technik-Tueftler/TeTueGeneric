"""All functions and features for logging the app
"""

import sys
from functools import partialmethod
from loguru import logger
from pydantic import BaseModel, FilePath


class WatcherConfiguration(BaseModel):
    """
    Configuration settings for generic_requests
    """

    log_level: str
    log_file_path: FilePath


def init_logging(conf_watcher: WatcherConfiguration) -> None:
    """Initialization of logging to create log file and set level at beginning of the app.

    Args:
        log_level (str): Configured log level
    """
    logger.remove()
    logger.level("EXTDEBUG", no=9, color="<bold><yellow>")
    logger.__class__.extdebug = partialmethod(logger.__class__.log, "EXTDEBUG")
    logger.add(conf_watcher.log_file_path, rotation="500 MB", level=conf_watcher.log_level)
    logger.add(sys.stdout, colorize=True, level=conf_watcher.log_level)
