# KlasCroller (가제)

*version 1.0.1
<div align="center">

 <img width="15%" src="https://user-images.githubusercontent.com/50646145/202891559-317bce94-7cac-4009-83cb-670e8bdf2eca.png"/>


 ### KlasCroller
 #### -광운대학교 재학생 전용 PC 프로그램입니다.-
 
 <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>
 <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>
 <img src="https://img.shields.io/badge/Matplotlib-11557C.svg?style=for-the-badge&logo=Matplotlib&logoColor=white"/>
 <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>
 <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"/>
 
</div>


## 프로젝트 설명
광운대학교 학부생들이 학업 성취도에 대한 진단을 스스로 할 수 있도록 Window 기반 GUI 프로그램을 만들었습니다.

사용자의 요청에 따라 파라미터를 기준으로 단일 학기 분석, 두 개 학기 비교, 전체 학기(완료된 학기 기준) 진단 등의 기능을 수행 합니다.

klas 로그인 시 사용하는 id,pw를 입력받아, 학부생의 학업 성취 데이터를 추출하여 아래와 같은 파라미터를 구성합니다. 


### [프로젝트 기간] 
- (2022-09-12 ~ 2022-11-26)


### [기능]
- KLAS (광운대학교 웹어플리케이션, https://klas.kw.ac.kr) 접근 및 로그인
- 학기별 출석율, 과제제출율, 성적 등의 학생 Data Scraping 및 파라미터 값 추출
      
      [파라미터]
    
      - 의지력 = (출석 / (출석+지각+결석)) X 100
  
      - 지능 = ((실제 취득 학점) / (취득 가능 학점) ) X 100
  
      - 생존력 = (*수강과목 갯수 에 따른 점수) + 총 과제,퀴즈 갯수(50개 이상 이면 50점)
  
      - 근명성 = (제출한 과제 수 + 제출한 퀴즈 수) / (총 과제 수 + 총 퀴즈 수) X 100
  
      - 가성비 = (지능 /의지력)
    
    
        *수강과목 갯수 에 따른 점수:
              6 개 이상: 50점
              5 개 : 40점
              4 개 : 32점
              3 개 : 24점
              2 개 : 16점
              1 개 : 8점 

- 로컬 PC에 cache file 생성 후 파라미터 값 저장 (이후 프로그램 구동 시, Scraping 과정 생략)
- 파라미터를 근거로 사용자가 원하는 학기에 대해 그래프 출력

      단일 학기 분석 시, 오각형 방사 그래프(Radiation Graph Of A Pentagon) 출력
      
      두개 학기 분석 시, 막대 그래프(Bar Graph) 출력
      
- 완료된 학기에 분석하여 사용자의 학업 성취 스타일 판단

        1. 5개의 파라미터 각각의 중앙값으로 가장 높은 값, 두번째로 높은 값을 가지는 파라미터를 확인
        
        2. 가장 높은 값을 가지는 파라미터로 적절한 동물 이미지를 매치 
        
        3. 두번째로 높은 값을 가지는 파라미터로 적절한 배경 이미지를 매치
        
        4. 2,3 번 으로 장점이 부각된 사용자의 학업 성취 스타일 출력
        
        5. 5개의 파라미터 각각의 중앙값으로 가장 낮은 값, 두 번째로 낮은 값을 가지는 파라미터를 확인
        
        6. 가장 낮은 값을 가지는 파라미터로 적절한 동물 이미지를 매치 
        
        7. 두번째로 낮은 값을 가지는 파라미터로 적절한 배경 이미지를 매치
        
        8. 6,7 번 으로 단점이 부각된 사용자의 학업 성취 스타일 출력

- 사용자 요청에 따른 cache file 초기화


### [사용법]
- KLAS 로그인 시 사용하는 id,pw로 프로그램에 로그인 해주세요. 
- 프로그램이 정상 작동이 되었다면 아래와 같은 화면에 사용자의 학번이 출력됩니다.

- <단일 학기 분석> 버튼을 클릭한다면, 해당 기능에 대한 설명과 학기 선택 콤보 박스가 있는 학기선택 창을 보실 수 있습니다. 
선택된 학기에 대해서 사용자의 파라미터 값으로 오각형의 방사그래프(Radiation Graph Of A Pentagon)가 출력됩니다.

- <두개 학기 비교> 버튼을 클릭한다면, 해당 기능에 대한 설명과 학기 선택 콤보 박스가 있는 학기선택 창을 보실 수 있습니다. 
선택된 두개 학기에 대해서 사용자의 파라미터 값으로 막대 그래프(Bar Graph)가 출력됩니다.

- <종합 평가> 버튼을 클릭한다면, 해당 기능에 대한 설명 창을 보실 수 있습니다. 

- 새 학기를 업데이트 하려거나, KLAS 정보를 local PC에 저장하고 싶지 않을 경우, <내 정보 초기화> 버튼을 클릭 해주세요. 

