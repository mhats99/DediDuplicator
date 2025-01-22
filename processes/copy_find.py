from model import Data
from collections import Counter


def copy_find_processes(data: Data) -> Data:

    hash_list = data.get_hash_list()
    count = Counter(hash_list)
    repetitive = [item for item, freq in count.items() if freq > 1]
    result = Data()
    result.set_data(sorted(data.get_hash_to_info(repetitive), key=lambda x: x.file_hash))
    return  result
