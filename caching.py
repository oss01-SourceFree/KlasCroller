import pickle
import gzip
import os

class CacheManager:
    def __init__(self,path,id):
        # 파일이름
        self.file_path = os.path.join(path,id+".plk")
    
    def SaveCache(self, data):
        # 저장, 압축
        with gzip.open(self.file_path, "wb") as f: 
            pickle.dump(data, f)
    
    # 저장된 데이터 초기화
    def InitCache(self):
        empty_dic = {} 
        with gzip.open(self.file_path, "wb") as f: 
            pickle.dump(empty_dic, f)
    
    # 저장된 데이터 가져오기
    def GetCache(self):
        dic = {} 
        with gzip.open(self.file_path,'rb') as f:
            dic = pickle.load(f)
        return dic
    
    # 파일 삭제
    def DestoryFile(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)