from tkinter import *
import os
import sys
from functools import partial

# 상대 경로 -> 절대 경로
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class WindowManager():
    def __init__(self, user_info = {}):
        self.id = ''
        self.pw = ''
        
        # 유저 정보 ( 의지력 , 지능 , 생존력 , 근명성 , 가성비)
        self.user_info = user_info
        # 전체(완료+현재) 학기 이름 (ex) 2022년 1학기)
        self.seme_list = list(user_info.keys())
        # 전체(완료+현재) 학기 수
        self.cnt_seme = len(user_info)
        
        # 선택창에서 유저가 선택한 학기의 인덱스
        self.semester_1 = 0
        self.semester_2 = 0
    
    def __del__(self):
        print()
        
    # 로그인 용 Window 설정
    def SetWindow_Login(self):
        # 창 설정
        self.win_lo = Tk()
        self.win_lo.title("Klas Log-in")
        self.win_lo.geometry("425x650")
        self.win_lo.option_add("*Font", "맑은고딕 25")
        
        # 하위 컴포넌트 선언
        # Button: 1
        # Label: 4
        # Entry: 2
        # PhotoImage : 1
        self.button_lo = Button(self.win_lo)
        self.label_lo = [Label(self.win_lo) for _ in range(4)]
        self.entry_lo = [Entry(self.win_lo) for _ in range(2)]
        self.img_lo = PhotoImage(master = self.win_lo)

        # id 라벨
        self.label_lo[1].config(text = "ID")
        # id 입력
        self.entry_lo[0] = Entry(self.win_lo, relief = "groove")
        self.entry_lo[0].insert(0,"학번을 입력하세요.")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.entry_lo[0].get() == "학번을 입력하세요.":
                self.entry_lo[0].delete(0, len(self.entry_lo[0].get()))
        self.entry_lo[0].bind("<Button-1>",clear)
        # pw 라벨
        self.label_lo[2] = Label(self.win_lo)
        self.label_lo[2].config(text = "Password")
        # pw 입력
        self.entry_lo[1] = Entry(self.win_lo)
        self.entry_lo[1].config(show="*")
        # 광운대학교 로고
        self.img_lo.config(file = resource_path("KlasCroller\\img\\kwang.png"))
        self.img_lo = self.img_lo.subsample(1)
        self.label_lo[0].config(image = self.img_lo)
        # 로그인 버튼
        self.button_lo.config(text="로그인",width=5,command=self.EventHandler_Login)

    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
        self.SetWindow_Login()
        self.label_lo[0].grid(row=1, column=2)
        self.label_lo[1].grid(row=3, column=2)
        self.entry_lo[0].grid(row=4, column=2)
        self.label_lo[2].grid(row=5, column=2)
        self.entry_lo[1].grid(row=6, column=2)
        self.button_lo.grid(row=7, column=2)
        self.label_lo[3].grid(row=7, column=2)
        self.win_lo.mainloop()

    def GetIdPw(self):
        self.OpenWindow_Login()
        return self.id,self.pw

    # 로그인 이벤트 핸들러
    def EventHandler_Login(self):
        self.id = self.entry_lo[0].get()
        self.pw = self.entry_lo[1].get()
        self.win_lo.destroy()
        
    # 메인메뉴 창 설정
    def SetWindow_MainMenu(self):
        # 창 설정
        self.win_main = Tk()
        self.win_main.title("Main Menu")
        self.win_main.geometry("650x400") # 가로 세로
        self.win_main.option_add("*Font", "맑은고딕 25")
        
        # 하위 컴포넌트 선언
        # Button : 3
        # Label : 1
        self.button_main = [Button(self.win_main) for _ in range(3)]
        self.label_main = Label(self.win_main)
        
        # 라벨 설정
        self.label_main.config(text="기능 선택")
        
        # 버튼 설정
        self.button_main[0].config(text = "한 학기\n 분석",command = self.OpenWindow_SelectOne)
        self.button_main[1].config(text = "학기 간 \n비교 분석", command = self.FuncEventHandler2)
        self.button_main[2].config(text = "학점 mbti", command = self.FuncEventHandler3)
    
    # 메인메뉴 창 열기
    def OpenWindow_MainMenu(self):
        self.SetWindow_MainMenu()
        self.label_main.pack()
        self.button_main[0].place(x=5,y=80,height=290,width=210)
        #self.label_main.place(x=7,y=85,height=100,width=100)
        self.button_main[1].place(x=220,y=80,height=290,width=210)
        self.button_main[2].place(x=435,y=80,height=290,width=210)
        self.win_main.mainloop()
    
    # 학기선택 창 설정
    def OpenWindow_SelectOne(self):
        # 창 설정
        self.win_select = Tk()
        self.win_select.title("학기 선택")
        self.win_select.geometry("400x300")
        self.win_select.option_add("*Font", "맑은고딕 25")
        
        # 하위 컴포넌트 선언
        # Button: 학기 수 만큼
        # Label: 1
        self.label_select = Label(self.win_select)
        self.button_select = [Button(self.win_select) for _ in range(self.cnt_seme)]
        
        # 라벨 설정
        self.label_select.config(text = "한 개의 학기를 선택하세요.")
        
        # 버튼 설정
        for i in range(self.cnt_seme):
            self.button_select[i].config(text = self.seme_list[i]
                                        ,command = partial(self.OpenWindow_OneSemesterAnalysis, i))
            
        # 출력
        self.label_select.pack()
        for i in range(self.cnt_seme):
            self.button_select[i].pack()
        self.win_select.mainloop()

    def OpenWindow_OneSemesterAnalysis(self,semster):
        # 창 설정
        win_osa = Tk()
        win_osa.title("한 학기 분석")
        win_osa.geometry("400x300")
        win_osa.option_add("*Font", "맑은고딕 25")
        # 하위 컴포넌트 선언
        # Label : 2
        label_osa = [Label(win_osa) for _ in range(3)]
        
        # 라벨 설정
        label_osa[1].config(text= "한 학기 분석")
        label_osa[1].config(text= str(self.seme_list[semster]))
        label_osa[2].config(text= str(self.user_info[self.seme_list[semster]]))
        
        for i in range(3):
            label_osa[i].pack()

    
    # 두번째 기능 선택 이벤트 핸들러
    def FuncEventHandler2(self):
        self.win_sem2 = Tk()
        self.win_sem2.title("Klas semester2")
        self.win_sem2.geometry("400x300")
        self.win_sem2.option_add("*Font", "맑은고딕 25")
        self.label1 = Label(self.win_sem2, text = "학기 간 비교 분석하기")
        self.label1.pack()

    # 세번째 기능 선택 이벤트 핸들러
    def FuncEventHandler3(self):
        self.win_sem3 = Tk()
        self.win_sem3.title("Klas semester3")
        self.win_sem3.geometry("400x300")
        self.win_sem3.option_add("*Font", "맑은고딕 25")
        idx = len(self.sem_list)-1
        self.label1 = Label(self.win_sem3, text = self.sem_list[idx] + "학기 학점 결과보기")
        self.label1.pack()
        
