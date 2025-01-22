import hashlib

class FileHash():
    
    def __init__(self,package_size:int = 64) -> bytes:
         
         self.__package_size = package_size*1024
         
    def file_hash(self,file_path:str, hash_algorithm:str = 'blake2b') -> bytes:
        
        hasher = getattr(hashlib, hash_algorithm)()
        
        with open(file_path, 'rb') as file:
            chunk_size = self.__package_size
            while chunk := file.read(chunk_size):
                    hasher.update(chunk)
            del chunk,chunk_size
        
        return hasher.digest()