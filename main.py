# -*- coding: utf-8 -*-
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import multiprocessing as mp

# 버전정보
# python 3.10.7
# chrome 105.0.5195.127

from scraping import Scraper
from displaying import *
from caching import CacheManager

# 상대 경로 -> 절대 경로
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    
    # 유저 정보가 담긴 파일 위치
    path_user_file = resource_path("KlasCroller\\usr")

    loginWin = WindowManager()
    alert = SubBoxManager()

    # 사용자로부터 id,pw를 받아온다.
    id,pw = loginWin.GetIdPw()
    del loginWin
    
    # loading box 출력(SubProcess, 동시실행을 위해서)
    proc = mp.Process(target=alert.LoadingBox, args=("ID,PW 유효성 검사 중 입니다..","1",), daemon=True)
    proc.start()
    
    # klas에 접속해서 id, pw 가 유효한지 먼저 확인
    scraper = Scraper(True)
    cache = CacheManager(path_user_file,id)
    file_name = os.path.join(path_user_file,str(id)+".plk")
    
    # 유효성 검사 중, 네트웨크에 제대로 연결되지 않았다면 강제 종료
    if(scraper.AcceseKlas(id,pw) == -1):
        proc.kill()
        del scraper, cache
        alert.MessageBox("인터넷 연결 불안으로 비정상 종료되었습니다.  다시 시도해주세요.")
        del alert
        os._exit(0)
    
    # id,pw가 유효하지 않다면 강제 종료
    if(scraper.AcceseKlas(id,pw) == -2):
        proc.kill()
        del scraper, cache
        alert.MessageBox("ID 혹은 Passward가 유효하지 않습니다.  다시 접속해주세요.")
        del alert
        os._exit(0)
    
    # 유효하다면 id로 캐시파일이 있는지 확인
    else:
        proc.kill()
        del scraper
        
        proc1 = mp.Process(target=alert.LoadingBox, args=("Klas에서 정보를 가져옵니다..","5",), daemon=True)
        proc1.start()
        scraper = Scraper()
        
        # (학번).plk 파일 이 없다면, 스크래핑 후 파일을 만든다.
        if not os.path.isfile(file_name):
            
            # 로그인 중, 네트웨크에 제대로 연결되지 않았다면 강제 종료
            if(scraper.AcceseKlas(id,pw) == -1):
                proc.kill()
                del scraper, cache
                alert.MessageBox("인터넷 연결 불안으로 비정상 종료되었습니다.  다시 시도해주세요.")
                del alert
                os._exit(0)
                    
            user_info = scraper.ProcessingUserData()
            proc1.kill()
            # 정보를 가져오는 동안, 네트웨크에 제대로 연결되지 않았다면 강제 종료
            if(user_info == -1):
                del scraper,cache
                alert.MessageBox("인터넷 연결 불안으로 비정상 종료되었습니다. 다시 시도해주세요.")
                del alert
                os._exit(0)
            # 정상적으로 읽어왔다면 캐시파일 생성
            del scraper
            cache.SaveCache(user_info)
        
        # (학번).plk 파일 이 있다면, 로딩 창 끄기.
        else:
            del scraper
            proc1.kill()
    
    user_info = cache.GetCache()
    display_main = WindowManager(user_info,id)
    display_main.Run_Main()