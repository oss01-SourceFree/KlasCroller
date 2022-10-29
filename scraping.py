# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Scraper:
    def __init__(self):
        self.url = "https://klas.kw.ac.kr/"
        '''
        창을 띄우지 않으려면 아래 # options.add_argument('headless') 코드의 주석을 해제하면 됩니다.
        '''
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    
    def accese_klas(self,id,pw):
        # 1. chrome창을 띄어, klas로 이동 
        self.browser.get(self.url)
        # 2. id, pw 입력
        self.browser.find_element(By.ID,"loginId").send_keys(id)
        self.browser.find_element(By.ID,"loginPwd").send_keys(pw)
        # 3. 로그인 버튼 클릭
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()





# url = "https://klas.kw.ac.kr/"

# '''
# 창을 띄우지 않으려면 아래 # options.add_argument('headless') 코드의 주석을 해제하면 됩니다.
# '''
# options = webdriver.ChromeOptions()
# # options.add_argument('headless')

# browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# # Klas 를 열고, 로그인을 수행하는 함수
# def accese_klas(id,pw):
#     # 1. chrome창을 띄어, klas로 이동 
#     browser.get(url)
#     # 2. id, pw 입력
#     browser.find_element(By.ID,"loginId").send_keys(id)
#     browser.find_element(By.ID,"loginPwd").send_keys(pw)
#     # 3. 로그인 버튼 클릭
#     browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()
    
#     return browser

# # 과목명을 가져오는 함수
# def scrape_subjectName(browser):
#     try:
#         elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"left")))
#         subject = list(set([name.text.split()[0] for name in elem]))
#         for str in subject:
#             if '-' in str:
#                 sub_str = str.split('-') 
#                 if sub_str[0].isdigit() and sub_str[1].isdigit():
#                     subject.remove(str)
#         return subject
#     except:
#         print('error!')
