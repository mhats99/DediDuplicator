from model import Data
from module.ui_tool import Worker
from .file_info import once_files_info, files_info_params
from module import FileHash
from typing import Callable



def files_info_worker(
    worker: Worker,
    directory: list[str],
    result: Data,
    set_progressbar:Callable,
):
    hash_class = FileHash()
    params = files_info_params(directory, result,hash_class)
    set_progressbar(0,len(params),0)
    worker.set_task(once_files_info, params)
    worker.start()
