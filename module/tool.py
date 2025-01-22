from concurrent.futures import ThreadPoolExecutor
from typing import Callable
import math


class Tool:

    def multi_process(function: Callable, parameters: list | tuple) -> None | str:
        """Runs a function using multiple threads.

        Args:
        function (Callable): The function to be run.
        parameters (Union[List[Tuple], List[List]]): Parameters of the function.
        """
        with ThreadPoolExecutor(max_workers=len(parameters)) as executor:
            futures = [executor.submit(function, *param) for param in parameters]
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    return f"Bug: {e}"

    def convert_size(size_bytes: int) -> str:
        """Converts file sizes to string and displays them in units such as kilobytes and megabytes.

        Args:
            size_bytes (int): _description_

        Returns:
            str: _description_
        """

        if size_bytes == 0:
            return "0B"

        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)

        return f"{s} {size_name[i]}"
