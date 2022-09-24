# �ѱ� ���� ����
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

# webdriver ��ü ����(chrome â�� ���� �ʵ��� �ɼ� �ο�)
options = webdriver.ChromeOptions()
'''
ũ��â ���鼭 �۾��Ϸ��� �Ʒ� �ּ�( options.add_argument('headless')�� �ִ°� ) �����ϼ���.
'''
# options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# Klas�� ���� 
def accese_klas():
    # 1. chrome���� klas�� ���� 
    browser.get(url)
    # 2. id, pw �Է�
    browser.find_element(By.ID,"loginId").send_keys(id)
    browser.find_element(By.ID,"loginPwd").send_keys(pw)
    # 3. �α��� ��ư Ŭ��
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()

    return browser

# ������� �������� �Լ�
def scrape_subjectName(browser):
    # �α��� ���� ���ʰ��� �ƹ��͵� ���� �ʴ� �ð� ���� �߻��Ѵ�.
    # ���� 10�� �̻� �ƹ��͵� �ȳ����� �״�� browser ����.
    try:
        elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"left")))
        
        # ������ ������ ��ó���Ͽ� ������� 'subject' ��� list�� �Ҵ�
        subject = list(set([name.text.split()[0] for name in elem]))
        for str in subject:
            if '-' in str:
                sub_str = str.split('-') 
                if sub_str[0].isdigit() and sub_str[1].isdigit():
                    subject.remove(str)
        return subject
    
    except:
        print('error!')