# -*- coding: utf-8 -*-
# �ѱ� ���� ����
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# ���� ����
# python 3.10.7
# chrome 105.0.5195.127

from scraping import *

browser = accese_klas()

# ����� �����ͼ� ���
subject_list = scrape_subjectName(browser)
print(subject_list)

# �⼮���� �����ͼ� ���

# �¶��� ���� ���� �����ͼ� ���

# ��������Ʈ ���� ���� �����ͼ� ���

# ���� ���� �����ͼ� ���

# ���� ���� �����ͼ� ���

# ���� ���� �����ͼ� ���