# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import time
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.url = "https://klas.kw.ac.kr/"
        '''
        창을 띄우지 않으려면 아래 # options.add_argument('headless') 코드의 주석을 해제하면 됩니다.
        '''
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        
        # 화면 전환시 데이터가 바로 로드되지 않아 scraping 되지 않는 문제를 막기위해
        # scaping 대상 페이지에 도착시 sleep() 사용, 아래 변수는 sleep()에 전달할 인자
        self.sleeping_time = 0.3
    
    
    
    
    
    
    def AcceseKlas(self,id,pw):
        # 1. chrome창을 띄어, klas로 이동 
        self.browser.get(self.url)
        # 2. id, pw 입력
        self.browser.find_element(By.ID,"loginId").send_keys(id)
        self.browser.find_element(By.ID,"loginPwd").send_keys(pw)
        # 3. 로그인 버튼 클릭
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()
        
        
        
        
        
    def ChangeSemester(self, semester_idx):
        time.sleep(self.sleeping_time)
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        element_dropdown = self.browser.find_element(By.CLASS_NAME,"form-control.form-control-sm")
        select_semster = Select(element_dropdown)
        select_semster.select_by_index(semester_idx)
        
        
        
        
        
        
    # 특정학기를 입력으로 받아 과목 정보를 가져온다.
    def ScrapingSubjectData(self,semester_idx):
        self.ChangeSemester(semester_idx)
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml') #html.parser
        
        # each_subject_list: 과목별 정보 (이차원 배열)
        # [첫번째 과목정보, 두번째 과목정보,…] 순으로 정리되어있다. 
        each_subject_list = list()
                
        # subjects_info: 반환할 결과
        # [수행한 팀플과제 수, 총 팀플과제 수, 
        #  제출한 개인과제 수, 총 개인과제 수,
        #  제출한 퀴즈 수, 총 퀴즈 수,
        #  출석횟수, 결석횟수, 지각횟수] 순으로 정리되어있다. 
        subjects_info = [0 for _ in range(9)]
        
        # subjects: 특정 학기에 들은 과목들에 정보가 들어있다.    
        subjects = soup.find("ul",{"class":"subjectlist listbox"}).findAll("li")
        
        for i in range(1,len(subjects)+1):
            time.sleep(self.sleeping_time)
            if(not self.WaitPageChange("scheduletitle")):
                return 0
            
            self.ChangeSemester(semester_idx)
            xpath = "/html/body/main/div/div/div/div/div[1]/div[2]/ul/li["+str(i)+"]"
            each_subject_list.append(self.GetEachSubjectsData(xpath))
        
        for i in range(len(subjects)):
            if each_subject_list[i] == -1:   #오류가 반환되었을 시, 일단 그냥 패쓰
                continue
            for j in range(9):
                subjects_info[j] += each_subject_list[i][j]
        
        
        print(semester_idx)
        print(subjects_info)
        
    
    
    
    
    
    
    # Klas에서 사용자의 Data를 가져와 가공한다.
    def ProcessingUserData(self):
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml') #html.parser

        print("0차 ㅇㅋ")

        
        # cnt_semesters: (진행 + 완료) 학기 갯수
        semesters = soup.find("select",{"class":"form-control form-control-sm"}).findAll("option")
        cnt_semesters = len(semesters)
        
        print("1차 ㅇㅋ")
        
        # 여기서부터 학기를 변경하며 과목 정보를 추출한다.

        
        print("2차 ㅇㅋ")
        
        for semester_i in range(cnt_semesters):
            print()
            self.ScrapingSubjectData(semester_i)
            print("=========================================")
        
        print("성공!!")
        
        
        
        
        
        
    # 특정 과목의 정보를 반환한다. (팀플, 과제, 퀴즈 참여율, 출석율)
    def GetEachSubjectsData(self, xpath):
        self.browser.find_element(By.XPATH,xpath).click()
        time.sleep(self.sleeping_time)

        if(not self.WaitPageChange('oval')):
            exit(0)
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        res = list() # 최종 결과를 담을 변수
        
        # 학업참여정보
        present = soup.select('a > span.oval')
        team_project = re.findall(r'\d+', str(present[1]))      # 팀플
        assignment = re.findall(r'\d+', str(present[5]))        # 과제
        quiz = re.findall(r'\d+', str(present[6]))              # 퀴즈

        # 출결 정보
        attendance = len(soup.select('table > tbody > tr > td > span.memberft01'))  # 출석
        absent = len(soup.select('table > tbody > tr > td > span.memberft04'))      # 결석
        late = len(soup.select('table > tbody > tr > td > span.memberft02'))        # 지각
        vacancy = len(soup.select('table > tbody > tr > td > span.memberft05'))     # 공결
        
        self.browser.get(self.url)
        
        res = [int(x) for x in team_project]
        res += [int(x) for x in assignment]
        res += [int(x) for x in quiz]
        res.append((attendance + vacancy))  # 공결은 출석으로 포함
        res.append(absent)
        res.append(late)
        
        return res
    
    
    
    
    
    
    # 어떤 class 이름을 입력으로 주면 해당 class 이름이 현재 url 페이지에 나타날 때까지 기다린다.
    # 10 초 안에 나타나면 True 반환, 10 초 이상 안나타나며 False 반환
    def WaitPageChange(self,class_name):
        try:
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,class_name)))
        except:
            print("error")
            return False
        return True
    