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
    """
    Configuration settings for generic HTTP requests in test cases
    """

    request_timeout: int = 30


class WatcherConfiguration(BaseSettings):
    """
    Configuration settings for watcher in test cases
    """

    log_level: str = "INFO"
    log_file_path: str = "files/app.log"


class Configuration(BaseSettings):
    """
    Configuration settings in test cases
    """

    gen_req: GenReqConfiguration
    watcher: WatcherConfiguration


config = Configuration(gen_req=GenReqConfiguration(), watcher=WatcherConfiguration())


@pytest.fixture(name="loguru_caplog")
def fct_loguru_caplog():
    """
    Pytest fixture to capture and return Loguru log output.

    This fixture sets up a custom log capture mechanism for Loguru. It removes all existing
    handlers, adds a new StringIO handler to capture logs, and then yields this handler for
    use in tests. After the test, it cleans up by removing the added handler.

    """
    logger.remove()
    log_output = io.StringIO()
    logger.add(log_output, colorize=True, level="DEBUG")
    yield log_output
    logger.remove()


@pytest.mark.asyncio
async def test_generic_http_request_success(mocker):
    """
    Test the successful execution of the generic_http_request function.

    This asynchronous test verifies that the generic_http_request function correctly
    handles a successful HTTP GET request. It uses mocking to simulate a server response
    and checks if the function processes this response correctly.

    Args:
        mocker (pytest_mock.MockFixture): Pytest fixture for mocking.

    Test Procedure:
        1. Mock the HTTP GET request to return a successful response.
        2. Call the generic_http_request function with test parameters.
        3. Assert that the response matches the expected mock response.

    Assertions:
        - The response is not None.
        - The response status code is 200.
        - The response text is "Success".

    Notes:
        - This test uses the @pytest.mark.asyncio decorator to handle asynchronous testing.
        - The requests.get method is mocked to avoid actual network calls during testing.
        - The test assumes the existence of a 'config' object, which should be defined
          or mocked in the broader test setup.
    """
    # Procedure 1: Mock the HTTP GET request to return a successful response
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.text = "Success"
    mocker.patch("src.requests.get", return_value=mock_response)

    # Procedure 2: Call the generic_http_request function with test parameters
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)

    # Procedure 3: Assert that the response matches the expected mock response
    assert response is not None, "Response is None"
    assert response.status_code == 200, "Status code is not 200"
    assert response.text == "Success", "Response text is not 'Success'"


@pytest.mark.asyncio
async def test_generic_requests_connect_timeout(mocker, loguru_caplog):
    """
    Test the generic_http_request function's behavior when a connection timeout occurs.

    This asynchronous test verifies that the generic_http_request function correctly
    handles a connection timeout scenario. It uses mocking to simulate a timeout error
    and checks if the function logs the appropriate error message.

    Args:
        mocker (pytest_mock.MockFixture): Pytest fixture for mocking.
        loguru_caplog (io.StringIO): Custom fixture to capture Loguru log output.

    Test Procedure:
        1. Mock the HTTP GET request to raise a ConnectTimeout exception.
        2. Call the generic_http_request function with test parameters.
        3. Assert that the function returns None and logs the expected error message.

    Assertions:
        - The function returns None when a timeout occurs.
        - The appropriate error message is logged.

    Notes:
        - This test uses the @pytest.mark.asyncio decorator for asynchronous testing.
        - The requests.get method is mocked to raise a ConnectTimeout exception.
        - The test checks both the return value and the logged output to ensure
          correct error handling and reporting.
    """
    # Procedure 1: Mock the HTTP GET request to raise a ConnectTimeout exception
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectTimeout("Test timeout error"),
    )

    # Procedure 2: Call the generic_http_request function with test parameters
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)

    # Procedure 3: Assert that the function returns None and logs the expected error message
    assert response is None, "Response is not None"
    assert (
        "Connection timeout error occurred" in loguru_caplog.getvalue()
    ), "Error message not found in log output"


@pytest.mark.asyncio
async def test_generic_requests_http_error(mocker, loguru_caplog):
    """
    Test the generic_http_request function's behavior when an HTTP error occurs.

    This asynchronous test verifies that the generic_http_request function correctly
    handles an HTTP error scenario (e.g., a 4xx or 5xx status code). It uses mocking
    to simulate an HTTPError exception and checks if the function logs the
    appropriate error message and returns None.

    Args:
        mocker (pytest_mock.MockFixture): Pytest fixture for mocking.
        loguru_caplog (io.StringIO): Custom fixture to capture Loguru log output.

    Test Procedure:
        1. Mock the HTTP GET request to raise an HTTPError exception.
        2. Call the generic_http_request function with test parameters.
        3. Assert that the function returns None and logs the expected error message.

    Assertions:
        - The function returns None when an HTTP error occurs.
        - The appropriate error message ("HTTP error occurred") is logged.

    Notes:
        - This test uses the @pytest.mark.asyncio decorator for asynchronous testing.
        - The requests.get method is mocked to raise an HTTPError exception, simulating
          a server returning an error status code.
        - This test specifically checks that the correct error message is logged to
          provide visibility into the failure.
    """
    # Procedure 1: Mock the HTTP GET request to raise an HTTPError exception
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.HTTPError("Test http error"),
    )

    # Procedure 2: Call the generic_http_request function with test parameters
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)

    # Procedure 3: Assert that the function returns None and logs the expected error message
    assert response is None, "Response is not None"
    assert (
        "HTTP error occurred" in loguru_caplog.getvalue()
    ), "Error message not found in log output"


@pytest.mark.asyncio
async def test_generic_requests_connection_error(mocker, loguru_caplog):
    """
    Test the generic_http_request function's behavior when a connection error occurs.

    This asynchronous test verifies that the generic_http_request function correctly
    handles a connection error scenario. It uses mocking to simulate a ConnectionError
    exception and checks if the function logs the appropriate error message and returns None.

    Args:
        mocker (pytest_mock.MockFixture): Pytest fixture for mocking.
        loguru_caplog (io.StringIO): Custom fixture to capture Loguru log output.

    Test Procedure:
        1. Mock the HTTP GET request to raise a ConnectionError exception.
        2. Call the generic_http_request function with test parameters.
        3. Assert that the function returns None and logs the expected error message.

    Assertions:
        - The function returns None when a connection error occurs.
        - The appropriate error message ("Connection error occurred") is logged.

    Notes:
        - This test uses the @pytest.mark.asyncio decorator for asynchronous testing.
        - The requests.get method is mocked to raise a ConnectionError exception, simulating
          network issues or inability to establish a connection to the server.
        - This test ensures that the function gracefully handles connection failures and
          provides appropriate logging for debugging purposes.
    """
    # Procedure 1: Mock the HTTP GET request to raise a ConnectionError exception
    mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError("Test connection error"),
    )
    # Procedure 2: Call the generic_http_request function with test parameters
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header, config)

    # Procedure 3: Assert that the function returns None and logs the expected error message
    assert response is None, "Response is"
    assert (
        "Connection error occurred" in loguru_caplog.getvalue()
    ), "Error message not found in log output"
