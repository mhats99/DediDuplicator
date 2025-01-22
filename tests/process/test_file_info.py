import pytest

from processes.file_info import once_files_info

from tests.config import Test_Config
from model import Data
from module import FileHash


def test_once_files_info():

    hash_class = FileHash()
    data = Data()

    once_files_info(hash_class, data, Test_Config.FILE_PATH)

    assert len(data) == 1
    assert data.get_name_to_info(Test_Config.FİLE_NAME)[0].path == Test_Config.FILE_PATH
    assert data.get_name_to_info(Test_Config.FİLE_NAME)[0].name == Test_Config.FİLE_NAME
    assert type(data.get_name_to_info(Test_Config.FİLE_NAME)[0].file_hash) == bytes


if __name__ == "__main__":
    pytest.main()
