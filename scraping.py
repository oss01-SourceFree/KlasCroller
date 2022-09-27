# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 테스트할 때 KLAS id와 pw를 입력하세요.
# 깃허브 올릴 때, id,pw 꼭 지우고 업로드!!!  
url = "https://klas.kw.ac.kr/"
id = '2017203088'
pw = 'dldbstls1!'

'''
창을 띄우지 않으려면 아래 # options.add_argument('headless') 코드의 주석을 해제하면 됩니다.
'''
options = webdriver.ChromeOptions()
# options.add_argument('headless')


# 좌측에 탐색기에서 chromedriver.exe 위에 커서를 두고 오른쪽 키를 누루면 [경로복사] 가 있습니다.
# 해당 경로를 아래 chromedriver_path 에 저장하세요.
# (단, \ 를 /로 바꿔야 합니다.)
chromedriver_path = "C:/Users/2youn/Desktop/OSS_cpy/KlasCroller/chromedriver.exe"
browser = webdriver.Chrome(chromedriver_path ,options=options)

# Klas 를 열고, 로그인을 수행하는 함수
def accese_klas():
    # 1. chrome창을 띄어, klas로 이동 
    browser.get(url)
    # 2. id, pw 입력
    browser.find_element(By.ID,"loginId").send_keys(id)
    browser.find_element(By.ID,"loginPwd").send_keys(pw)
    # 3. 로그인 버튼 클릭
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()
    
    return browser

# 과목명을 가져오는 함수
def scrape_subjectName(browser):
    try:
        elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"left")))
        subject = list(set([name.text.split()[0] for name in elem]))
        for str in subject:
            if '-' in str:
                sub_str = str.split('-') 
                if sub_str[0].isdigit() and sub_str[1].isdigit():
                    subject.remove(str)
        return subject
    except:
        print('error!')