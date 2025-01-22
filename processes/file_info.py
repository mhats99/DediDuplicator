from module import FileTool, FileHash
from config import FileInfoProcessesVar
from model import Data, FileInfoData

def once_files_info(hash_class: FileHash, result: Data, file_path: str):

    try:
        file_info: FileInfoData = FileTool.get_file_info(file_path)
        file_info.file_hash = hash_class.file_hash(file_path)
        result.add(file_info)
    except Exception as e:
        return f"{FileInfoProcessesVar.PROCESS_ERROR} {file_path}: {str(e)}"

def files_info_params(directory: list[str], result: Data, hash_class:FileHash) -> list[list[FileHash,Data,str]]:
   
    files_path = []

    for i in directory:
        files_path.extend(FileTool.get_all_files(i))

    once_params = []

    for file_path in files_path:
        once_params.append([hash_class, result, file_path])
        
    return once_params

