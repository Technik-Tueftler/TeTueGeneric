"""All functions and features for logging the app
"""

import sys
from functools import partialmethod
from pathlib import Path
from loguru import logger
from pydantic import BaseModel


class WatcherConfiguration(BaseModel):
    """
    Configuration model for the watcher component.

    This class inherits from Pydantic's BaseModel and defines the configuration
    parameters for logging in the watcher component.

    Attributes:
        log_level (str): The logging level to be used (e.g., "DEBUG", "INFO", "WARNING").
        log_file_path (str | pathlib.Path): The file path where log files will be stored.
    """

    log_level: str
    log_file_path: str | Path


def init_logging(conf_watcher: WatcherConfiguration) -> None:
    """
    Initializes logging configuration for the application..  

    Args:
        conf_watcher (watcher.WatcherConfiguration): A configuration object containing 
        logging settings.

    Returns:
        None

    Note:
        - This function modifies the global `logger` object from Loguru.
        - The 'EXTDEBUG' level is set to 9, between DEBUG (10) and INFO (20).
        - Log files are rotated when they reach 500 MB in size.
        - Console output is colorized for better readability.

    """
    logger.remove()
    logger.add(conf_watcher.log_file_path, rotation="500 MB", level=conf_watcher.log_level)
    logger.add(sys.stdout, colorize=True, level=conf_watcher.log_level)
