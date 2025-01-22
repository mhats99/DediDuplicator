import pytest

from module import Tool
from unittest.mock import MagicMock


def test_multi_process():

    def sample_function(x, y):
        return x + y

    mock_function = MagicMock(side_effect=sample_function)

    parameters = [(1, 2), (3, 4), (5, 6)]

    Tool.multi_process(mock_function, parameters)

    assert mock_function.call_count == len(parameters)

    mock_function.assert_any_call(1, 2)
    mock_function.assert_any_call(3, 4)
    mock_function.assert_any_call(5, 6)


def test_cover_size():

    assert Tool.convert_size(1) == "1.0 B"
    assert Tool.convert_size(1024) == "1.0 KB"
    assert Tool.convert_size(1024**2) == "1.0 MB"
    assert Tool.convert_size(1024**3) == "1.0 GB"
    assert Tool.convert_size(1024**4) == "1.0 TB"


if __name__ == "__main__":
    pytest.main()
