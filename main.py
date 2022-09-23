# -*- coding: utf-8 -*-
# 한글 깨짐 방지
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 버전 정보
# python 3.10.7
# chrome 105.0.5195.127

from scraping import *

browser = accese_klas()

# 과목명 가져와서 출력
subject_list = scrape_subjectName(browser)
print(subject_list)

# 출석정보 가져와서 출력

# 온라인 강의 정보 가져와서 출력

# 팀프로젝트 강의 정보 가져와서 출력

# 시험 정보 가져와서 출력

# 과제 정보 가져와서 출력

# 퀴즈 정보 가져와서 출력