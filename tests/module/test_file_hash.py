import pytest

from module import FileHash
from tests.config import Test_Config


def test_file_hash():

    result_0 = FileHash().file_hash(Test_Config.FILE_PATH)
    result_1 = FileHash().file_hash(Test_Config.FILE_PATH)
    assert result_0 == result_1


if __name__ == "__main__":
    pytest.main()
