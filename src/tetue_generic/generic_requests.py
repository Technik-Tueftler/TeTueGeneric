"""Implement generic request function with own logging and return functionality
"""
from __future__ import annotations
import requests
from . import watcher
from . import REQUEST_TIMEOUT


async def generic_http_request(
    url: str, header: dict, logger: watcher.loguru.Logger = None
) -> requests.Response:
    """Function for http requests with all possible exceptions which are then stored by a logger.

    Args:
        url (str): The URL to send the request
        header (dict): The headers to include in the request
        logger (watcher.loguru.Logger): Logger for storing the error

    Returns:
        requests.Response: Return value from http request or in failure case a None
    """
    try:
        return requests.get(url, headers=header, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.HTTPError as err:
        if logger is not None:
            watcher.logger.error(f"HTTP error occurred: {err}")
        else:
            print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.ConnectTimeout as err:
        if logger is not None:
            watcher.logger.error(f"Connection timeout error occurred: {err}")
        else:
            print(f"Connection timeout error occurred: {err}")
        return None
    except requests.exceptions.ConnectionError as err:
        if logger is not None:
            watcher.logger.error(f"Connection error occurred: {err}")
        else:
            print(f"Connection error occurred: {err}")
        return None


async def generic_http_reques2(a: int, b: int):
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if a < b:
        raise ValueError("Fehler")
    return a-b
