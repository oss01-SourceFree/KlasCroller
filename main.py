# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 버전정보
# python 3.10.7
# chrome 105.0.5195.127

from scraping import *
from displaying import *

#사용자로부터 id,pw를 받아온다.
id = 0
pw =''

id,pw = getIdPw()

if(id != 0 and pw != ''):
    browser = accese_klas(id,pw)

    # 과목명 list를 가져와서 출력한다.
    subject_list = scrape_subjectName(browser)
    print(subject_list)

