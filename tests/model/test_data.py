import pytest
from model import FileInfoData, Data


class TestData:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.__fhash = b"1234567890abcdef"
        self.__fpath = "/path/to/file"
        self.__fname = "file.txt"
        self.__fcreation = 5747358356835
        self.__fsize = "1MB"
        self.__fselect = False

    def multiple_data(self, data_instance: Data | list, element: int):

        for i in range(element):
            file_info_data: FileInfoData = FileInfoData(
                self.__fhash + i.to_bytes(),
                self.__fpath + str(i),
                self.__fname + str(i),
                self.__fcreation + i,
                self.__fsize + str(i),
                self.__fselect,
            )
            if type(data_instance) == Data:
                data_instance.add(file_info_data)
            else:
                data_instance.append(file_info_data)
            del file_info_data

    def test_add(self):

        file_info_data: FileInfoData = FileInfoData(
            self.__fhash,
            self.__fpath,
            self.__fname,
            self.__fcreation,
            self.__fsize,
            self.__fselect,
        )

        data_instance: Data = Data()
        data_instance.add(file_info_data)
        assert len(data_instance.get_name_list()) == 1
        assert data_instance.get_name_list()[0] == file_info_data.name

    def test_get_hash_list(self):

        data_instance: Data = Data()
        element = 50
        self.multiple_data(data_instance, element)
        hash_list = data_instance.get_hash_list()

        assert len(hash_list) == element
        for i in range(element):
            assert hash_list[i] == self.__fhash + i.to_bytes()

    def test_get_name_list(self):

        data_instance: Data = Data()
        element = 50
        self.multiple_data(data_instance, element)
        name_list = data_instance.get_name_list()

        assert len(name_list) == element
        for i in range(element):
            assert name_list[i] == self.__fname + str(i)

    def test_get_hash_to_info(self):

        data_instance: Data = Data()
        element = 50
        self.multiple_data(data_instance, element)
        copy_element = 7

        for i in range(element + 1, element + copy_element + 1):
            data = FileInfoData(
                file_hash=self.__fhash,
                path=self.__fpath + str(i),
                name=self.__fname + str(i),
                creation_time=self.__fcreation + i,
                size=self.__fsize + str(i),
            )
            data_instance.add(data)

        result = data_instance.get_hash_to_info(self.__fhash)
        assert len(result) == copy_element
        for i in result:
            assert i.file_hash == self.__fhash
            assert i.path != self.__fpath
            assert i.name != self.__fname
            assert i.creation_time != self.__fcreation
            assert i.size != self.__fsize

    def test_get_name_to_info(self):

        data_instance: Data = Data()
        element = 50
        self.multiple_data(data_instance, element)
        file_info_data = FileInfoData(
            file_hash=self.__fhash,
            path=self.__fpath,
            name=self.__fname,
            creation_time=self.__fcreation,
            size=self.__fsize,
        )
        data_instance.add(file_info_data)
        result = data_instance.get_name_to_info(self.__fname)

        assert len(result) == 1
        assert result[0] == file_info_data

    def test_get_hash_to_info_no_match(self):
        data_instance: Data = Data()
        result = data_instance.get_hash_to_info([b"nonexistenthash"])
        assert len(result) == 0

    def test_get_name_to_info_no_match(self):
        data_instance: Data = Data()
        result = data_instance.get_name_to_info(["nonexistentfile.txt"])
        assert len(result) == 0

    def test_set_data(self):

        data_instance: Data = Data()
        element = 50
        data_list = []
        self.multiple_data(data_list, element)
        data_instance.set_data(data_list)

        assert len(data_instance) == element
        for i in data_instance:
            assert type(i) == FileInfoData

    def test_get_grouping_by_hash(self):

        data_instance: Data = Data()
        element = 50
        self.multiple_data(data_instance, element)
        group_hash = data_instance.get_grouping_by_hash()

        for i in group_hash:
            hash_value = i[0].file_hash
            for val in i:
                assert hash_value == val.file_hash


if __name__ == "__main__":
    pytest.main()
