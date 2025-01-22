import pytest


from processes import copy_find_processes, files_info_multi
from tests.config import Test_Config
from model import Data
from collections import Counter


def test_copy_find():

    data = Data()
    path_list = [Test_Config.FOLDER_PATH, Test_Config.FOLDER_PATH_2]

    files_info_multi(path_list, data)
    copy_files = copy_find_processes(data)

    assert type(copy_files) == Data
    assert len(copy_files) > 1
    assert len(copy_files) == len(Counter([i.path for i in copy_files]))


if __name__ == "__main__":
    pytest.main()
