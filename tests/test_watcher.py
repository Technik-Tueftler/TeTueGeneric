import pytest
from loguru import logger
import sys
import io
from pathlib import Path
import src

src.init_logging(src.WatcherConfiguration(log_level="TRACE", log_file_path="test_log.log"))

@pytest.fixture(name="capture_logs")
def fct_capture_logs():
    output = []
    handler_id = src.logger.add(output.append, level="TRACE")
    yield output
    logger.remove(handler_id)

# def test_log(capture_logs):
#     src.logger.debug("Test DEBUG 1 message 1")
#     src.logger.debug("Test DEBUG 2 message 2")
#     print(capture_logs)
#     assert "Test DEBUG message 2\n" in capture_logs[1]

def test_init_logging(capture_logs):
    src.logger.debug("Test DEBUG message")
    src.logger.info("Test INFO message")
    src.logger.extdebug("Test EXTDEBUG message")
    print(capture_logs)
    print(src.logger.level)
    
    assert src.logger.level("EXTDEBUG").no == 9
    assert src.logger.level("EXTDEBUG").color == "<bold><yellow>"
    assert "Test INFO message" in capture_logs[1]
    assert "Test DEBUG message" in capture_logs[0]
    assert "Test EXTDEBUG message" in capture_logs[2]
