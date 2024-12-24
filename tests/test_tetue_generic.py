"""
This file contains unit tests for verifying the functionality of 
generic utilities and functions within package tetue_generic.
"""
import sys
import pytest
from asyncmock import AsyncMock
import src

sys.path.append('..')

@pytest.mark.asyncio
async def test_generic_http_request_success(mocker):
    """
    Tests the successful execution of a generic HTTP request.

    This test verifies that the `generic_http_request` function behaves correctly
    when an HTTP request succeeds. Using mocking, it simulates the behavior of an 
    HTTP GET request to ensure that the function:
    - Returns a valid response.
    - Correctly processes the response's status code and text.

    Args:
        mocker: A fixture used to mock modules and functions, 
        applied here to patch `src.requests.get`.

    Test Steps:
    1. Create a mock HTTP response with a status code of 200 and the text "Success."
    2. Patch the `src.requests.get` function to return the mock response.
    3. Call the `generic_http_request` function with a sample URL and headers.
    4. Validate the returned response to ensure that:
        - It is not `None`.
        - It contains a status code of 200.
        - It includes the text "Success."
    """
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.text = "Success"
    mocker.patch("src.requests.get", return_value=mock_response)

    url = "https://example.com"
    header = {"Authorization": "Bearer token"}
    response = await src.generic_http_request(url, header)

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Success"


@pytest.mark.asyncio
async def test_generic_requests_http_error(mocker, capsys):
    """
    Tests the behavior of `generic_http_request` when an HTTP error occurs.

    This test ensures that the `generic_http_request` function handles HTTP errors gracefully by:
    - Returning `None` when an HTTP error is encountered.
    - Logging the appropriate error message to standard output.

    Args:
        mocker: A fixture used to mock modules and functions, 
        here used to simulate an HTTP error by patching `requests.get`.
        capsys: A pytest fixture for capturing and inspecting standard output and error streams.

    Test Steps:
    1. Mock the `requests.get` function to raise an `HTTPError` when called.
    2. Provide a sample URL and headers to the `generic_http_request` function.
    3. Verify the following:
        - The function returns `None`.
        - The error message "HTTP error occurred: \n" is logged to the standard output.
    """

    mocker.patch("requests.get", side_effect=src.requests.exceptions.HTTPError)
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}

    # with pytest.raises(src.requests.exceptions.HTTPError):
    response = await src.generic_http_request(url, header)
    captured = capsys.readouterr()
    assert response is None
    assert captured.out == "HTTP error occurred: \n"


@pytest.mark.asyncio
async def test_generic_requests_connect_timeout(mocker, capsys):
    """
    Tests the behavior of `generic_http_request` when a connection timeout occurs.

    This test ensures that the `generic_http_request` function handles connection timeouts 
    gracefully by:
    - Returning `None` when a `ConnectTimeout` exception is raised.
    - Logging the appropriate timeout error message to standard output.

    Args:
        mocker: A fixture used to mock modules and functions, 
        here used to simulate a connection timeout by patching `requests.get`.
        capsys: A pytest fixture for capturing and inspecting standard output and error streams.

    Test Steps:
    1. Mock the `requests.get` function to raise a `ConnectTimeout` exception when called.
    2. Provide a sample URL and headers to the `generic_http_request` function.
    3. Verify the following:
        - The function returns `None`.
        - The error message "Connection timeout error occurred: \n" 
        is logged to the standard output.
    """

    mocker.patch("requests.get", side_effect=src.requests.exceptions.ConnectTimeout)
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}

    response = await src.generic_http_request(url, header)
    captured = capsys.readouterr()
    assert response is None
    assert captured.out == "Connection timeout error occurred: \n"


@pytest.mark.asyncio
async def test_generic_requests_connection_error(mocker, capsys):
    """
    Tests the behavior of `generic_http_request` when a connection error occurs.

    This test ensures that the `generic_http_request` function handles 
    connection errors appropriately by:
    - Returning `None` when a `ConnectionError` exception is raised.
    - Logging the correct connection error message to standard output.

    Args:
        mocker: A fixture used to mock modules and functions, 
        here used to simulate a connection error by patching `requests.get`.
        capsys: A pytest fixture for capturing and inspecting standard output and error streams.

    Test Steps:
    1. Mock the `requests.get` function to raise a `ConnectionError` exception when called.
    2. Provide a sample URL and headers to the `generic_http_request` function.
    3. Verify the following:
        - The function returns `None`.
        - The error message "Connection error occurred: \n" is logged to the standard output.
    """

    mocker.patch("requests.get", side_effect=src.requests.exceptions.ConnectionError)
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}

    response = await src.generic_http_request(url, header)
    captured = capsys.readouterr()
    assert response is None
    assert captured.out == "Connection error occurred: \n"

def test_gen_req_configuration_default():
    """
    Verifies the default value for request timeout of `GenReqConfiguration`.

    Steps:
    1. Instantiate `GenReqConfiguration`.
    2. Assert that `request_timeout` equals 10.
    """
    config = src.GenReqConfiguration()
    assert config.request_timeout == 10

def test_init_generic_requests_changes_timeout():
    """
    Validates whether `init_generic_requests` correctly updates the timeout value.

    Steps:
    1. Set a new timeout value.
    2. Call `init_generic_requests` with the new value.
    3. Assert that the `request_timeout` in `gen_req_settings` is updated.
    """
    new_timeout = 20
    src.init_generic_requests(new_timeout)
    assert src.gen_req_settings.request_timeout == new_timeout

def test_init_generic_requests_invalid_value():
    """
    Ensures `init_generic_requests` raises an error for invalid input.

    Steps:
    1. Pass an invalid timeout value.
    2. Assert that a `ValueError` is raised.
    """
    with pytest.raises(ValueError):
        src.init_generic_requests(-1)

def test_watcher_configuration_default():
    """
    Verifies the default value for file path of `WatcherConfiguration`.

    Steps:
    1. Instantiate `WatcherConfiguration`.
    2. Assert that `log_file_path` equals files/app.log.
    """
    config = src.WatcherConfiguration()
    assert config.log_file_path == "files/app.log"

def test_init_generic_watcher_changes_file_path():
    """
    Validates whether `init_generic_watcher` correctly updates the file path.

    Steps:
    1. Set a new file path.
    2. Call `init_generic_watcher` with the new value.
    3. Assert that the `log_file_path` in `watcher_settings` is updated.
    """
    new_file_path = "test/app2.log"
    src.init_generic_watcher(new_file_path)
    assert src.watcher_settings.log_file_path == "test/app2.log"
