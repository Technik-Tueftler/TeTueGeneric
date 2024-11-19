import sys
import pytest
from asyncmock import AsyncMock
import src

sys.path.append('..')

@pytest.mark.asyncio
async def test_generic_http_request_success(mocker):
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
    mocker.patch("requests.get", side_effect=src.requests.exceptions.ConnectTimeout)
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}

    response = await src.generic_http_request(url, header)
    captured = capsys.readouterr()
    assert response is None
    assert captured.out == "Connection timeout error occurred: \n"


@pytest.mark.asyncio
async def test_generic_requests_connection_error(mocker, capsys):
    mocker.patch("requests.get", side_effect=src.requests.exceptions.ConnectionError)
    url = "https://example.com"
    header = {"Authorization": "Bearer token"}

    response = await src.generic_http_request(url, header)
    captured = capsys.readouterr()
    assert response is None
    assert captured.out == "Connection error occurred: \n"