from model import FileInfoData


class Data:

    def __init__(self) -> None:
        self.__data: list[FileInfoData] = []

    def add(self, data: FileInfoData):
        """Adds a FileInfoData instance to the data list."""
        self.__data.append(data)

    def get_hash_list(self) -> list[bytes]:
        """Returns a list of file hashes."""
        return [i.file_hash for i in self.__data]

    def get_name_list(self) -> list[str]:
        """Returns a list of file names."""
        return [i.name for i in self.__data]

    def get_hash_to_info(self, file_hash: list[bytes]) -> list[FileInfoData]:
        """Returns a list of FileInfoData instances that match the given file hashes."""
        return [item for item in self.__data if item.file_hash in file_hash]

    def get_name_to_info(self, name: list[str]) -> list[FileInfoData]:
        """Returns a list of FileInfoData instances that match the given names."""
        return [item for item in self.__data if item.name in name]

    def get_grouping_by_hash(self) -> list[FileInfoData]:
        
        return [self.get_hash_to_info(i) for i in set(self.get_hash_list())]

    def get_path_to_info(self,path: list[str]):
        
        return [item for item in self.__data if item.path in path]
    
    def set_data(self,data:list[FileInfoData]):
        
        self.__data = data
    
    def __len__(self):
        """Returns the number of FileInfoData instances in the data list."""
        return len(self.__data)

    def __getitem__(self, index):
        """Allows indexing to access FileInfoData instances."""
        return self.__data[index]

    def __iter__(self):
        """Allows iteration over the data list."""
        return iter(self.__data)

    def __repr__(self):
        """Returns a string representation of the Data instance."""
        return f"Data({len(self.__data)} items)"