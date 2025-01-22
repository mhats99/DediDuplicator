import pytest

from processes import files_info_multi

from tests.config import Test_Config
from model import Data
from module import FileTool
from collections import Counter


def test_files_info_multi():

    data = Data()
    path_list = [Test_Config.FOLDER_PATH, Test_Config.FOLDER_PATH_2]

    files_info_multi(path_list, data)

    files_path_list = []
    for i in path_list:
        files_path_list.extend(FileTool.get_all_files(i))
    assert len(data) == len(files_path_list)

    assert len(Counter(data.get_hash_list())) > 1
    assert len(Counter(data.get_name_list())) > 1


if __name__ == "__main__":
    pytest.main()
