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
    
    # loading box 출력(SubProcess, 동시실행을 위해서)
    proc = mp.Process(target=alert.LoadingBox, daemon=True)
    proc.start()
    
    cache = CacheManager(path_user_file,id)
    file_name = os.path.join(path_user_file,str(id)+".plk")
    
    # (학번).plk 파일 이 없거나 파일 속 딕셔너리가 비었다면, klas에 로그인, 스크래핑 후 파일을 만든다.
    if not os.path.isfile(file_name):
        # 입력한 id,pw로 klas에 로그인 될 때까지 반복
        success_login = False
        while(not success_login):
            scraper = Scraper()
            if(scraper.AcceseKlas(id,pw) != -1):
                success_login = True
            else:
                del scraper
                id,pw = loginWin.GetIdPw()
        
        # 로그인 완료되면, 데이터 가져오기 (제대로 스크랩이 안된다면 -1 반환)
        user_info = scraper.ProcessingUserData()
        del loginWin
        del scraper
        
        # user_info == -1 이라면 알림창 출력 후 프로그램 종료
        if(user_info == -1):
            proc.kill()
            alert.MessageBox("인터넷 연결이 원활하지 않아 비정상 종료되었습니다. 다시 시도해 주십시오.")
            os._exit(0)
        
        cache.SaveCache(user_info)
    
    # 로딩창 제거(SubProcess 종료)
    proc.kill()
    
    # user_info : 유저 정보가 담긴 dictionary
    user_info = cache.GetCache()
    print(user_info)
    # main 창을 띄울 객체 선언, user 정보 전달
    mainWin = WindowManager(user_info)
    mainWin.OpenWindow_MainMenu()
    
    os._exit(0)
    




