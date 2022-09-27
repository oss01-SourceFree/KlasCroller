# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 버전정보
# python 3.10.7
# chrome 105.0.5195.127

from scraping import *

browser = accese_klas()

# 과목명 list를 가져와서 출력한다.
subject_list = scrape_subjectName(browser)
print(subject_list)

