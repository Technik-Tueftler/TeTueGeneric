"""Implement generic request function with own logging and return functionality
"""

from __future__ import annotations
import requests
from pydantic import BaseModel, PositiveInt
from . import watcher


class GenReqConfiguration(BaseModel):
    """
    Configuration settings for generic_requests
    """

    request_timeout: PositiveInt = 10


gen_req_settings = GenReqConfiguration()


def init_generic_requests(request_timeout: int) -> None:
    """
    Locale initialization for the transfer of default values 
    for the generic request functions 

    Args:
        request_timeout (int): Time until a request is canceled 
    """
    if request_timeout <= 0:
        raise ValueError("request_timeout must be greater than 0")
    gen_req_settings.request_timeout = request_timeout


async def generic_http_request(
    url: str, header: dict, logger: watcher.loguru.Logger = None
) -> requests.Response:
    """Function for http requests with all possible exceptions which are then stored by a logger.

    Args:
        url (str): The URL to send the request
        header (dict): The headers to include in the request
        logger (loguru.logger): Logger for storing the error

    Returns:
        requests.Response: Return value from http request or in failure case a None
    """
    try:
        return requests.get(
            url, headers=header, timeout=gen_req_settings.request_timeout
        )
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
