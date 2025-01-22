class FileInfoData:
    def __init__(
        self,
        file_hash: bytes,
        path: str,
        name: str,
        creation_time: int,
        size: str,
        selected: bool = False,
    ):
        self.file_hash = file_hash
        self.path = path
        self.name = name
        self.creation_time = creation_time
        self.size = size
        self.selected = selected
