# -*- coding: utf-8 -*-
# 한글 깨짐 방지
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://klas.kw.ac.kr/"
id = ''
pw = ''

# webdriver 객체 생성(chrome 창이 뜨지 않도록 옵션 부여)
options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# Klas에 접근 
def accese_klas():
    # 1. chrome에서 klas로 접근 
    browser.get(url)
    # 2. id, pw 입력
    browser.find_element(By.ID,"loginId").send_keys(id)
    browser.find_element(By.ID,"loginPwd").send_keys(pw)
    # 3. 로그인 버튼 클릭
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()

    return browser

# 과목명을 가져오는 함수
def scrape_subjectName(browser):
    # 로그인 직후 몇초간의 아무것도 뜨지 않는 시간 텀이 발생한다.
    # 만약 10초 이상 아무것도 안나오면 그대로 browser 종료.
    try:
        elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"left")))
        
        # 가져온 정보를 전처리하여 과목명만 'subject' 라는 list에 할당
        subject = list(set([name.text.split()[0] for name in elem]))
        for str in subject:
            if '-' in str:
                sub_str = str.split('-') 
                if sub_str[0].isdigit() and sub_str[1].isdigit():
                    subject.remove(str)
        return subject
    
    except:
        print('error!')