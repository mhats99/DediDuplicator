import pytest

from model import FileInfoData

fname = "test.file"
fhash = b"bc16a54b859c4f635898fc3d6131f86cdeea51000bbbfa7bdc21627c588a1d3c"
fcreation = 1247457487
fpath = "C:\\user\\test.file"
fsize = "113450"


def test_file_info_data():

    fid = FileInfoData(fhash, fpath, fname, fcreation, fsize)

    assert fid.name == fname
    assert fid.file_hash == fhash
    assert fid.creation_time == fcreation
    assert fid.path == fpath
    assert fid.size == fsize

    assert type(fid.name) == str
    assert type(fid.file_hash) == bytes
    assert type(fid.creation_time) == int
    assert type(fid.path) == str
    assert type(fid.size) == str


if __name__ == "__main__":
    pytest.main()
