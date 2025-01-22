from .file_info import once_files_info,files_info_params
from model import Data
from module import Tool,FileHash

def files_info_multi(directory: list[str], result: Data):
    """Returns information about all files in the given directory."""
    
    hash_class = FileHash()
    Tool.multi_process(once_files_info, files_info_params(directory,result,hash_class))