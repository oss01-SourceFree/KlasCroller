# KlasCroller

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


# 프로젝트 설명
_* 광운대학교 2022년 2학기 <오픈소스소프트웨어개발> 교과목의 14조 팀프로젝트 결과물입니다._

 - 제안서: [[14조]프로젝트_제안서.pdf](https://github.com/oss01-SourceFree/KlasCroller/files/10095838/14._.pdf)
 - 중간보고서: [[14조]중간보고서.pdf](https://github.com/oss01-SourceFree/KlasCroller/files/10095834/14.pdf)
 - 최종보고서: [[14조]최종_보고서.pdf](https://github.com/oss01-SourceFree/KlasCroller/files/10096442/14._.pdf)


광운대학교 학부생들이 학업 성취도에 대한 진단을 스스로 할 수 있도록 Window 기반 GUI 프로그램을 만들었습니다.

KLAS(광운대학교 웹 어플리케이션) 로그인 시 사용하는 id,pw를 입력받아, 학부생의 학업 성취 데이터를 추출하여 파라미터를 구성합니다.

사용자의 요청에 따라 파라미터를 기준으로 다양한 기능을 수행 합니다.

## [프로젝트 기간] 
- (2022-09-12 ~ 2022-11-26)

## [대상]
- klas에 교과목 수강기록과 성적 정보가 입력되어있는 광운대학교 재학생
- (수강 기록에 e-learing 과목이 포함되어 있을 시, 프로그램이 정상 동작되지 않습니다.)

## [Flow Chart]
<div align="center">
<img width="50%" src="https://user-images.githubusercontent.com/50646145/204094979-3a39ee60-0cd6-4c20-9fd7-70e629908eef.png"/>
</div>

## [기능]
- KLAS (광운대학교 웹어플리케이션, https://klas.kw.ac.kr) 로그인을 통하여 사용자가 입력한 id,pw 유효성 검사
<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/50646145/204077513-16a98a97-a26c-4f21-81ee-278b8a397f89.png"/>
</div>


- id,pw 가 유효하다면 klas에 접근하여 아래 기능을 수행 (유효하지 않은 id,pw 가 입력되었다면, 프로그램 종료)


_-id,pw가 유효할 경우_
<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/50646145/204077514-c7d7661f-4a02-40ed-a77e-26e008ac12bd.png"/>
 </div>
 
_-id,pw가 유효하지 않을 경우_
<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/50646145/204078492-d0622831-8343-498c-8090-720ac87118ad.png"/>
</div>




- 학기별 출석율, 과제제출율, 성적 등의 학생 Data Scraping 및 파라미터 값 추출
      
      [파라미터]
    
      - 의지력 = (출석 / (출석+지각+결석)) X 100
  
      - 사고력 = ((실제 취득 학점) / (취득 가능 학점) ) X 100
  
      - 생존력 = (*수강과목 갯수 에 따른 점수) + 총 과제,퀴즈 갯수(50개 이상 이면 50점)
  
      - 근명성 = (제출한 과제 수 + 제출한 퀴즈 수) / (총 과제 수 + 총 퀴즈 수) X 100
  
      - 가성비 = (사고력 /의지력)
    
    
        *수강과목 갯수 에 따른 점수:
              6 개 이상: 50점
              5 개 : 40점
              4 개 : 32점
              3 개 : 24점
              2 개 : 16점
              1 개 : 8점 


- Data Scraping 중 문제 발생 시, 메시지 창 출력 후 프로그램 종료

<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/50646145/204078623-c63f8b0b-b1a3-403d-95eb-184670555bb8.png"/>
</div>



- 로컬 PC에 cache file 생성 (파일이름은 '<학번>.plk') 후 파라미터 값 저장 (이후 프로그램 구동 시, Scraping 과정 생략)



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


_++사용자의 장점이 부각된 동물 이미지 : ['소나무', '돌고래', '쥐', '개미', '네잎클로버']_

<div align="center", float= "left", margin="auto">
<img width="15%" src="https://user-images.githubusercontent.com/50646145/204079827-54328bdc-78fc-4a0a-b5ac-958a3893b667.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079828-bb34f473-5a0d-40dd-957e-5060284d6e24.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079829-630e9896-da41-41d2-9bf9-482415902dc3.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079830-2e9ad240-10c3-48a8-9f7a-4be30c8b0459.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079831-391a53a8-f6c9-432c-8731-f09ad1956658.png"/>
</div>

_++사용자의 단점이 부각된 동물 이미지 : ['베짱이', '금붕어', '게복치', '나무늘보', '까마귀']_
<div align="center", float= "left", margin="auto">
<img width="15%" src="https://user-images.githubusercontent.com/50646145/204079921-4c7c5170-8812-4328-9b5f-5c6affa8b5b1.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079923-895ff548-72ba-4d5e-a8c8-89f08f83e730.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079924-8d3ffdd9-aaa9-4860-be80-2d042de808a1.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079936-bf5e4c12-3713-4357-9386-f65a67dcd708.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204079927-add85346-d1c9-4b48-b6dd-de833fa0cdf2.png"/>
</div>

_++사용자의 장점이 부각된 형용어 : ['열정많은', '저명한', '끈질긴', '부지런한', '운 좋은']_
<div align="center", float= "left", margin="auto">
<img width="15%" src="https://user-images.githubusercontent.com/50646145/204083325-e18a44d8-58d6-4f25-ba6b-cadf99d0d327.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083324-8091cd1b-23f7-44c5-9c39-a71f2cd8bf31.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083327-c70bc709-5b78-471d-a9b2-cb5dda1eb7ad.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083323-3bfdb87d-937d-4573-a9a4-4987cb917d40.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083321-d3edb1f3-a8ed-4d53-a572-382305ea1d40.png"/>
</div>

_++사용자의 단점이 부각된 형용어 : ['노력상실', '우둔한', '포기빠른', '게으른', '불운한']_
<div align="center", float= "left", margin="auto">
<img width="15%" src="https://user-images.githubusercontent.com/50646145/204083424-cdf5afbc-2e28-42a6-a3d9-0a3a55a11172.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083423-7ad0ea04-0ac5-46d3-8110-c33469c95423.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083422-a5e5da18-fccf-49c4-97fb-342c51c8cdda.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083420-50ce3102-f04e-405c-99a4-b82da9e6c859.png"/>
 <img width="15%" src="https://user-images.githubusercontent.com/50646145/204083419-050238b5-1c6b-4ace-a736-3097492bc8dc.png"/>
</div>




- 사용자로부터 관심있는 진로 분야를 입력받아, '잡코리아'(https://www.jobkorea.co.kr/) 로 연결


- 사용자 요청에 따른 cache file 초기화


## [실행방법]

1. 파이썬 설치 (https://www.python.org/downloads/)

2. visual studio 설치 (https://visualstudio.microsoft.com/ko/)

3. terminal을 열고 다음 명령어를 순서대로 수행
   - 'git clone https://github.com/oss01-SourceFree/KlasCroller.git'
   - 'cd ./KlasCroller'

4. 관련 라이브러리/모듈 설치
   (tkinter, matplotlib, numpy, selenium, beautifulsoup4, webdriver-manager 등)
   
5. 네이버 나눔 글꼴 설치 (https://hangeul.naver.com/font)
   
6. 'main.py' 실행

    -> [ Ctrl + Alt + N ] or [ 왼쪽 마우스 클릭 + 'Run Code' ]


## [사용법]
- KLAS 로그인 시 사용하는 id,pw로 프로그램에 로그인 해주세요. 
<div align="center", float= "left", margin="auto">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204079519-35f64d50-f2dd-490a-bd7f-cdf23fa490ab.png"/>
</div>

- 프로그램이 정상 작동이 되었다면 아래와 같은 화면에 사용자의 학번이 출력됩니다.
<div align="center", float= "left", margin="auto">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204078977-4bd7db65-ee4b-4314-bdb3-486804e2ea3d.png"/>
</div>

- {단일 학기 분석} 버튼을 클릭한다면, 해당 기능에 대한 설명과 학기 선택 콤보 박스가 있는 학기선택 창을 보실 수 있습니다. 
선택된 학기에 대해서 사용자의 파라미터 값으로 오각형의 방사그래프(Radiation Graph Of A Pentagon)가 출력됩니다.
<div align="center", float= "left", margin="auto">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204079180-4e49c686-0980-4ed6-8c83-8022249ee4cd.png"/>
<img width="45%" src="https://user-images.githubusercontent.com/50646145/204079185-89af32c4-8066-4ac6-9af9-a99c37e15e24.png"/>
</div>

- {두개 학기 비교} 버튼을 클릭한다면, 해당 기능에 대한 설명과 학기 선택 콤보 박스가 있는 학기선택 창을 보실 수 있습니다. 
선택된 두개 학기에 대해서 사용자의 파라미터 값으로 막대 그래프(Bar Graph)가 출력됩니다.
<div align="center", float= "left">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204079474-68a59dae-9145-4a48-aaad-bbfbd81db6ee.png"/>
<img width="45%" src="https://user-images.githubusercontent.com/50646145/204079483-915d0f45-4bc7-4d8e-95bf-44b3d65bbc41.png"/>
</div>

- {SF MBTI} 버튼을 클릭한다면, 해당 기능에 대한 설명을 보실 수 있습니다.
완료된 학기들을 종합적으로 평가하여 사용자의 학업 스타일과 어울리는 동물(+ 배경) 이미지가 출력됩니다.
<div align="center", float= "left">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204079459-e513121e-6cd7-4121-88ff-efe078f6a635.png"/>
<img width="45%" src="https://user-images.githubusercontent.com/50646145/204085394-f99a2d59-dc07-4e68-9772-4275438acd8e.png"/>
</div>

- {취업 공고 분야} 버튼을 클릭한다면, 해당 기능에 대한 설명을 보실 수 있습니다.
관심 있는 진로, 취업 분야의 키워드를 입력한 뒤 검색버튼을 누르면 '잡코리아'(웹사이트) 에서 해당 키워드에 대한 공고문을 바로 보실 수 있습니다.
<div align="center", float= "left">
<img width="25%" src="https://user-images.githubusercontent.com/50646145/204079436-ded25ba1-1e31-459a-b6b4-c4434d1ada2e.png"/>
</div>

- 새 학기를 업데이트 하려거나, KLAS 정보를 local PC에 저장하고 싶지 않을 경우, {내 정보 초기화} 버튼을 클릭 해주세요.
cache file 이 삭제되고, 프로그램이 종료 됩니다.
<div align="center", float= "left">
<img width="30%" src="https://user-images.githubusercontent.com/50646145/204079404-0fc7096a-2954-4301-a777-bb74b63d0fc0.png"/>
</div>
