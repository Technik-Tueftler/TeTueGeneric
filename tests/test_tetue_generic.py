"""
This file contains unit tests for verifying the functionality of
generic utilities and functions within package tetue_generic.
"""

import sys
import io
import requests
import pytest
from asyncmock import AsyncMock
from pydantic_settings import BaseSettings
from loguru import logger
import src

sys.path.append("..")


class GenReqConfiguration(BaseSettings):
    request_timeout: int = 30


class WatcherConfiguration(BaseSettings):
    log_level: str = "INFO"
    log_file_path: str = "files/app.log"


class Configuration(BaseSettings):
    gen_req: GenReqConfiguration
    watcher: WatcherConfiguration


config = Configuration(gen_req=GenReqConfiguration(), watcher=WatcherConfiguration())


@pytest.fixture(name="loguru_caplog")
def fct_loguru_caplog():
    logger.remove()
    log_output = io.StringIO()
    logger.add(log_output, colorize=True, level="DEBUG")
    yield log_output
    logger.remove()


@pytest.mark.asyncio
async def test_generic_http_request_success(mocker):
    """
    Tests the `generic_http_request` function to ensure it handles a successful 
    HTTP request correctly.

    This test:
    - Mocks the `requests.get` method to simulate a successful HTTP response with status code 200.
    - Verifies that the function returns a response object when the request is successful.
    - Checks that the response contains the expected status code and text.

    Args:
        mocker (pytest.MockFixture): Pytest mocker object for mocking functions and methods.

    Assertions:
        - The function's return value is not `None`.
        - The returned response has a status code of 200.
        - The returned response contains the expected text "Success".
    """
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.text = "Success"
    mocker.patch("src.requests.get", return_value=mock_response)

    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Success"


@pytest.mark.asyncio
async def test_generic_requests_connect_timeout(mocker, loguru_caplog):
    """
    Tests the `generic_http_request` function to ensure it handles a connection timeout correctly.

    This test:
    - Mocks the `requests.get` method to raise a `ConnectTimeout` exception.
    - Verifies that the function returns `None` when a timeout occurs.
    - Validates that the expected error message is present in the log output (via Loguru).

    Args:
        mocker (pytest.MockFixture): Pytest mocker object for mocking functions and methods.
        loguru_caplog (StringIO): Fixture for capturing log outputs from the Loguru logger.

    Assertions:
        - The function's return value is `None`.
        - The error message "Connection timeout error occurred" is present in the log output.
    """
    # async def test_generic_requests_connect_timeout(mocker, capsys):
    # src.init_logging(config.watcher) erste Version mit capsys
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectTimeout("Test timeout error"),
    )
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)
    assert response is None
    # assert "Connection timeout error occurred" in capsys.readouterr().out
    assert "Connection timeout error occurred" in loguru_caplog.getvalue()


@pytest.mark.asyncio
async def test_generic_requests_http_error(mocker, loguru_caplog):
    """
    Tests the `generic_http_request` function to ensure it handles HTTP errors correctly.

    This test:
    - Mocks the `requests.get` method to raise an `HTTPError` exception.
    - Verifies that the function returns `None` when an HTTP error occurs.
    - Validates that the expected error message is present in the log output (via Loguru).

    Args:
        mocker (pytest.MockFixture): Pytest mocker object for mocking functions and methods.
        loguru_caplog (StringIO): Fixture for capturing log outputs from the Loguru logger.

    Assertions:
        - The function's return value is `None`.
        - The error message "HTTP error occurred" is present in the log output.
    """
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.HTTPError("Test http error"),
    )
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)
    assert response is None
    assert "HTTP error occurred" in loguru_caplog.getvalue()


@pytest.mark.asyncio
async def test_generic_requests_connection_error(mocker, loguru_caplog):
    """
    Tests the `generic_http_request` function to ensure it handles connection errors correctly.

    This test:
    - Mocks the `requests.get` method to raise a `ConnectionError` exception.
    - Verifies that the function returns `None` when a connection error occurs.
    - Validates that the expected error message is present in the log output (via Loguru).

    Args:
        mocker (pytest.MockFixture): Pytest mocker object for mocking functions and methods.
        loguru_caplog (StringIO): Fixture for capturing log outputs from the Loguru logger.

    Assertions:
        - The function's return value is `None`.
        - The error message "Connection error occurred" is present in the log output.
    """
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError("Test connection error"),
    )
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)
    assert response is None
    assert "Connection error occurred" in loguru_caplog.getvalue()
