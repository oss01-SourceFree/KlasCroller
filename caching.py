import pickle
import gzip
import os

class CacheManager:
    def __init__(self):
        # 파일이름
        self.file_name = "important_info.pickle"
    
    def SaveCache(self, data):
        # 저장, 압축
        with gzip.open(self.file_name, "wb") as f: 
            pickle.dump(data, f)
    
    # 저장된 데이터 초기화
    def InitCache(self):
        empty_dic = {} 
        with gzip.open(self.file_name, "wb") as f: 
            pickle.dump(empty_dic, f)
    
    # 저장된 데이터 가져오기
    def GetCache(self):
        dic = {} 
        with gzip.open(self.file_name,'rb') as f:
            dic = pickle.load(f)
        print(dic)