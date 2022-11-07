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
        
        # self.num_semester: (진행 + 완료) 학기 갯수
        self.num_semester = 0
    
    # id와 pw를 입력받아 klas에서 로그인 실행
    def AcceseKlas(self,id,pw):
        # 1. chrome창을 띄어, klas로 이동 
        self.browser.get(self.url)
        # 2. id, pw 입력
        self.browser.find_element(By.ID,"loginId").send_keys(id)
        self.browser.find_element(By.ID,"loginPwd").send_keys(pw)
        # 3. 로그인 버튼 클릭
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()
        
        
        
    # Klas에서 사용자의 Data를 가져와 가공한다.
    def ProcessingUserData(self):
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml') #html.parser
        
        # sem_name: 학기 이름 ( ex) '2022년도 2학기' )
        # self.num_semester: (진행 + 완료) 학기 갯수
        semesters = soup.find("select",{"class":"form-control form-control-sm"}).findAll("option")
        self.num_semester = len(semesters)
        sem_name = {}
        for sem in semesters:
            sem_name.update({sem.text:[]})
        print(sem_name)
        
        # # academic_participation: 학기별 학업 참여도 (팀플,과제,퀴즈,출석율)
        # academic_participation = list()
        
        # # grade_information: 성적정보
        # grade_information = list()
        
        # for semester_i in range(self.num_semester):
        #     academic_participation.append(self.ScrapingSubjectData(semester_i))

        # print(academic_participation)
        
        # grade_information = self.ScrapingGradeData()
        # print(grade_information)
        
        
        
        
    # 특정학기를 입력받아 학업 참여도를 가져온다.
    def ScrapingSubjectData(self,semester_idx):
        self.ChangeSemester(semester_idx)
        
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml') #html.parser
        
        # each_subject_list: 과목별 정보
        # [첫번째 과목정보, 두번째 과목정보,…] 순으로 정리되어있다. 
        each_subject_list = list()
                
        # res: 반환할 결과
        # [수행한 팀플과제 수, 총 팀플과제 수, 
        #  제출한 개인과제 수, 총 개인과제 수,
        #  제출한 퀴즈 수, 총 퀴즈 수,
        #  출석횟수, 결석횟수, 지각횟수] 순으로 정리되어있다. 
        res = [0 for _ in range(9)]
        
        # subjects: 특정 학기에 들은 과목들에 정보가 들어있다.    
        subjects = soup.find("ul",{"class":"subjectlist listbox"}).findAll("li")
        
        for i in range(1,len(subjects)+1):
            if(not self.WaitPageChange("scheduletitle")):
                return 0
            
            self.ChangeSemester(semester_idx)
            xpath = "/html/body/main/div/div/div/div/div[1]/div[2]/ul/li["+str(i)+"]"
            each_subject_list.append(self.GetEachSubjectsData(xpath))
        
        for i in range(len(subjects)):
            if each_subject_list[i] == -1:   #오류가 반환되었을 시, 일단 그냥 패쓰
                continue
            for j in range(9):
                res[j] += each_subject_list[i][j]
                
        return res
    
    
    # 학기별 학업 참여도를 추출할 때, 학기 인덱스를 입력받아 해당 학기 페이지로 이동
    def ChangeSemester(self, semester_idx):
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        element_dropdown = self.browser.find_element(By.CLASS_NAME,"form-control.form-control-sm")
        select_semster = Select(element_dropdown)
        select_semster.select_by_index(semester_idx)
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        
    
    # 특정 한 학기의 특정 한 과목의 학업 참여도를 종합하여 반환한다. (팀플, 과제, 퀴즈, 출석율)
    def GetEachSubjectsData(self, xpath):
        self.browser.find_element(By.XPATH,xpath).click()
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
    
    
    
    # 성적정보를 가져온다.
    def ScrapingGradeData(self):
        if(not self.WaitPageChange("scheduletitle")):
            return 0
        
        self.browser.find_element(By.XPATH,"/html/body/header/div[1]/div/div[1]/button").click()
        time.sleep(self.sleeping_time)
        self.browser.find_element(By.XPATH,"/html/body/header/div[2]/div/div/div[1]/ul/li[2]/ul/li[2]/a").click()
        time.sleep(self.sleeping_time)
        
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'lxml') #html.parser
        
        tables = soup.select('div.tablelistbox > div#hakbu > table.AType')
        
        # 학점 가져오기
        credit = [[] for _ in range(len(tables))]
        for ta_idx,table in enumerate(tables):
            tbodies = table.select('td')
            for tbody in tbodies:
                if (' 3' in tbody.text):
                    credit[ta_idx].append(3)
                elif (' 2' in tbody.text):
                    credit[ta_idx].append(2) 
                elif (' 1' in tbody.text):
                    credit[ta_idx].append(1) 
        
        # 등급 가져오기
        grade = [[] for _ in range(len(tables))]
        for ta_idx,table in enumerate(tables):
            tbodies = table.select('td')
            for tbody in tbodies:
                if ('A+' in tbody.text):
                    grade[ta_idx].append(4.5)
                elif ('A0' in tbody.text):
                    grade[ta_idx].append(4.0)
                elif ('B+' in tbody.text):
                    grade[ta_idx].append(3.5) 
                elif ('B0' in tbody.text):
                    grade[ta_idx].append(3.0) 
                elif ('C+' in tbody.text):
                    grade[ta_idx].append(2.5) 
                elif ('C0' in tbody.text):
                    grade[ta_idx].append(2.0) 
                elif ('D+' in tbody.text):
                    grade[ta_idx].append(1.5) 
                elif ('D0' in tbody.text):
                    grade[ta_idx].append(1.0)
                elif ('F' in tbody.text):
                    grade[ta_idx].append(0) 
                elif ('P' in tbody.text):
                    grade[ta_idx].append(4.5)
        
        # res_1: 학기별 취득 가능 학점
        res_1 = [0 for _ in range(self.num_semester)]
        for i in range(self.num_semester):
            res_1[i] = sum(credit[i]) * 4.5
        
        # res_2: 학기별 실제 취득 학점
        res_2 = [0 for _ in range(self.num_semester)]
        for i in range(self.num_semester):
            # 성적처리가 안되었을 경우, -1 삽입
            if (len(grade[i]) != len(credit[i])):
                res_2[i] = -1
                continue
            for j in range(len(grade[i])):
                res_2[i] += (grade[i][j] * credit[i][j])
                
        # res : res_1 , res_2 종합
        # 학기별로 취득 가능 학점 , 실제 취득 학점 순으로 출력
        res = []
        for i in range(self.num_semester):
            res.append(res_2[i])
            res.append(res_1[i])
            
        return res
    
    
    # 어떤 class 이름을 입력으로 주면 해당 class 이름이 현재 url 페이지에 나타날 때까지 기다린다.
    # 10 초 안에 나타나면 데이터 로드할 시간을 좀 더 주고 True 반환, 10 초 이상 안나타나며 False 반환
    def WaitPageChange(self,class_name):
        try:
            WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,class_name)))
            time.sleep(self.sleeping_time)
        except:
            print("error")
            return False
        return True
    