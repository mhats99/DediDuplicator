import pytest
from datetime import datetime

import pytest
import os
import tempfile
import time

from module import FileTool
from tests.config import Test_Config


def test_get_file_info():

    file_path = Test_Config.FILE_PATH
    file_info = FileTool.get_file_info(file_path)

    assert file_info.path == str(file_path)
    assert file_info.name == Test_Config.FİLE_NAME
    assert type(file_info.size) == str
    assert datetime.strptime(
        time.ctime(file_info.creation_time), "%a %b %d %H:%M:%S %Y"
    )
    assert file_info.file_hash == None


def test_get_all_files():

    all_files = FileTool.get_all_files(Test_Config.FOLDER_PATH_2)
    assert len(all_files) == Test_Config.FOLDER_PATH_2_NUMBER
    assert type(all_files[0]) == str


@pytest.fixture
def temp_files():
    """Create temporary files for testing."""
    files = []
    for _ in range(3):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b"Test content")
        temp_file.close()
        files.append(temp_file.name)
    yield files
    # Clean up temporary files after tests
    for file_path in files:
        try:
            os.remove(file_path)
        except OSError:
            pass  # Ignore errors if the file was already deleted


def test_delete_existing_files(temp_files):
    """Test deleting existing files."""
    results = FileTool.delete_files(temp_files)
    assert all(
        result[1] for result in results
    ), "Some files were not deleted successfully."


def test_delete_non_existing_file():
    """Test deleting a non-existing file."""
    non_existing_file = "non_existing_file.txt"
    results = FileTool.delete_files([non_existing_file])
    assert results == [
        (non_existing_file, False)
    ], "Expected result for non-existing file not met."


def test_delete_with_error():
    """Test handling of errors during deletion."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        results = FileTool.delete_files([temp_dir])
        assert (
            results[0][1] is False
        ), "Expected failure when trying to delete a directory."
    finally:
        # Clean up the temporary directory
        try:
            os.rmdir(temp_dir)
        except OSError:
            pass  # Ignore errors if the directory was not empty


if __name__ == "__main__":
    pytest.main()
