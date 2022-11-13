# -*- coding: utf-8 -*-
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 버전정보
# python 3.10.7
# chrome 105.0.5195.127

from scraping import Scraper
from displaying import WindowManager

#임의로 설정한 학기 (리스트)
sem = ["2019-1", "2019-2","2020-1", "2020-2", "2021-1", "2021-2", "2022-1", "2022-2"]

#사용자로부터 id,pw를 받아온다.
loginWin = WindowManager(sem);

id,pw = loginWin.GetIdPw()

if(id != 0 and pw != ''):
    scraper = Scraper()
    scraper.AcceseKlas(id,pw)
    scraper.ProcessingUserData()
    # scraper.ScrapingGradeData()
    
    

# 종료 안되도록 넣은거
# os.system("pause")
