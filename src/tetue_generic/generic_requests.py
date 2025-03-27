"""Implement generic request function with own logging and return functionality"""

from __future__ import annotations
import requests
from pydantic import BaseModel, PositiveInt
from .watcher import logger


class GenReqConfiguration(BaseModel):
    """
    Configuration settings for generic HTTP requests.

    This class inherits from Pydantic's BaseModel and defines the configuration
    parameters for making generic HTTP requests.

    Attributes:
        request_timeout (PositiveInt): The timeout duration for HTTP requests in seconds.
                                       Must be a positive integer.

    Note:
        The use of PositiveInt ensures that the timeout value is always a positive integer,
        providing a safeguard against invalid timeout settings.
    """

    request_timeout: PositiveInt


async def generic_http_request(
    url: str, header: dict, config: BaseModel
) -> requests.Response | None:
    """
    Performs an asynchronous HTTP GET request and handles potential exceptions.

    This function sends a GET request to the specified URL with given headers and timeout.
    It catches and logs common HTTP request exceptions using Loguru.

    Args:
        url (str): The URL to send the GET request to.
        header (dict): A dictionary of HTTP headers to include in the request.
        config (pydantic.BaseModel): Configuration object containing request settings, 

    Returns:
        requests.Response | None: The response object if the request is successful, or 
        None if an exception occurs.

    Raises:
        No exceptions are raised; they are caught and logged instead.

    Logs:
        - HTTP errors
        - Connection timeout errors
        - General connection errors

    Note:
        This function uses a global `logger` object for logging, which should be
        a configured Loguru logger instance.
    """
    try:
        return requests.get(url, headers=header, timeout=config.gen_req.request_timeout)
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.ConnectTimeout as err:
        logger.error(f"Connection timeout error occurred: {err}")
        return None
    except requests.exceptions.ConnectionError as err:
        logger.error(f"Connection error occurred: {err}")
        return None
