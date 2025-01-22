import pytest
import os
from module import Logger
from tests.config import Test_Config


@pytest.fixture
def logger():
    if os.path.exists(Test_Config.LOG_FILE):
        try:
            os.remove(Test_Config.LOG_FILE)
        except PermissionError:
            pass

    logger_instance = Logger(Test_Config.LOG_FILE)

    yield logger_instance


def log_file_delete(logger_instance: Logger):

    for handler in logger_instance.logger.handlers:
        handler.close()
        logger_instance.logger.removeHandler(handler)


def test_singleton(logger):
    logger2 = Logger(Test_Config.LOG_FILE)
    assert logger is logger2
    log_file_delete(logger)


def test_log_level_setting(logger):
    logger.set_log_level("INFO")
    assert logger.logger.level == Logger._instance.logger.level
    log_file_delete(logger)


def test_log_format_setting(logger):
    format_string = "%(levelname)s: %(message)s"
    logger.set_log_format(format_string)
    for handler in logger.logger.handlers:
        assert handler.formatter._fmt == format_string
    log_file_delete(logger)


def test_debug_logging(logger):
    logger.debug("Debug message")
    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
    assert "Debug message" in log_content
    log_file_delete(logger)


def test_info_logging(logger):
    logger.info("Info message")
    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
    assert "Info message" in log_content
    log_file_delete(logger)


def test_warning_logging(logger):
    logger.warning("Warning message")
    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
    assert "Warning message" in log_content
    log_file_delete(logger)


def test_error_logging(logger):
    logger.error("Error message")
    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
    assert "Error message" in log_content
    log_file_delete(logger)


def test_critical_logging(logger):
    logger.critical("Critical message")
    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
    assert "Critical message" in log_content
    log_file_delete(logger)


def test_error_logging_with_exception(logger):

    try:
        faulty_function()

    except Exception as e:
        logger.error(str(e))

    with open(Test_Config.LOG_FILE, "r") as f:
        log_content = f.read()
        assert "name 'faulty_function' is not defined" in log_content
    log_file_delete(logger)


if __name__ == "__main__":
    pytest.main()
