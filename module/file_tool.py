import os
from model import FileInfoData
from .tool import Tool


class FileTool:

    def get_file_info(file_path: str) -> FileInfoData:
        """Returns the file name, size, and creation time based on the given file path.

        Args:
            file_path (str): _description_

        Raises:
            FileNotFoundError: _description_

        Returns:
            dict: _description_
        """

        if not os.path.isfile(file_path):
            raise FileNotFoundError

        file_stats = os.stat(file_path)

        file_i = FileInfoData(
            file_hash=None,
            path=file_path,
            name=os.path.basename(file_path),
            creation_time=file_stats.st_birthtime,
            size=Tool.convert_size(file_stats.st_size),
        )

        return file_i

    def get_all_files(directory: str) -> list[str]:
        """Returns the paths of all files in the specified directory."""

        file_paths = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_paths.append(os.path.join(root, file))

        return file_paths

    def delete_files(
        file_paths: list[str],
    ) -> list[tuple[str, bool] | tuple[None, False] | tuple[str, bool, str]]:
        """
        Deletes files specified by their full paths.

        :param file_paths: A list of full paths to the files to be deleted
        :return: A list of results indicating success or failure for each file
        """

        results = []
        for file_path in file_paths:
            try:
                if os.path.isfile(file_path): 
                    os.remove(file_path)  
                    results.append((file_path, True)) 
                else:
                    results.append((file_path, False))  
            except Exception as e:
                results.append((file_path, False, str(e)))  

        return results if results else [(None, False)]  
