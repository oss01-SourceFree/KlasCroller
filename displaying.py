from tkinter import *
from tkinter import ttk
import os
import sys
import matplotlib.pyplot as plt
from functools import partial

import time

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
    
    def __del__(self):
        print()

    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
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
        button_lo = Button(self.win_lo)
        label_lo = [Label(self.win_lo) for _ in range(4)]
        self.entry_lo = [Entry(self.win_lo) for _ in range(2)]
        img_lo = PhotoImage(master = self.win_lo)

        # id 라벨
        label_lo[1].config(text = "ID")
        # id 입력
        self.entry_lo[0] = Entry(self.win_lo, relief = "groove")
        self.entry_lo[0].insert(0,"학번을 입력하세요.")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.entry_lo[0].get() == "학번을 입력하세요.":
                self.entry_lo[0].delete(0, len(self.entry_lo[0].get()))
        self.entry_lo[0].bind("<Button-1>",clear)
        # pw 라벨
        label_lo[2] = Label(self.win_lo)
        label_lo[2].config(text = "Password")
        # pw 입력
        self.entry_lo[1] = Entry(self.win_lo)
        self.entry_lo[1].config(show="*")
        # 광운대학교 로고
        img_lo.config(file = resource_path("KlasCroller\\img\\kwang.png"))
        img_lo = img_lo.subsample(1)
        label_lo[0].config(image = img_lo)
        # 로그인 버튼
        button_lo.config(text="로그인",width=5,command=self.EventHandler_Login)
        
        # 출력
        label_lo[0].grid(row=1, column=2)
        label_lo[1].grid(row=3, column=2)
        self.entry_lo[0].grid(row=4, column=2)
        label_lo[2].grid(row=5, column=2)
        self.entry_lo[1].grid(row=6, column=2)
        button_lo.grid(row=7, column=2)
        label_lo[3].grid(row=7, column=2)
        self.win_lo.mainloop()

    def GetIdPw(self):
        self.OpenWindow_Login()
        return self.id,self.pw

    # 로그인 이벤트 핸들러
    def EventHandler_Login(self):
        self.id = self.entry_lo[0].get()
        self.pw = self.entry_lo[1].get()
        self.win_lo.destroy()
        
    # 메인메뉴 창 열기
    def OpenWindow_MainMenu(self):
        # 창 설정
        win_main = Tk()
        win_main.title("Main Menu")
        win_main.geometry("650x400") # 가로 세로
        win_main.option_add("*Font", "맑은고딕 25")
        
        # 하위 컴포넌트 선언
        # Button : 3
        # Label : 1
        button_main = [Button(win_main) for _ in range(3)]
        label_main = Label(win_main)
        
        # 라벨 설정
        label_main.config(text="기능 선택")
        
        # 버튼 설정
        button_main[0].config(text = "한 학기\n 분석",command = self.OpenWindow_SelectOne)
        button_main[1].config(text = "학기 간 \n비교 분석", command = self.OpenWindow_SelectTwo)
        button_main[2].config(text = "학점 mbti", command = self.FuncEventHandler3)
        
        label_main.pack()
        button_main[0].place(x=5,y=80,height=290,width=210)
        #label_main.place(x=7,y=85,height=100,width=100)
        button_main[1].place(x=220,y=80,height=290,width=210)
        button_main[2].place(x=435,y=80,height=290,width=210)
        win_main.mainloop()
    
    # 학기선택 창 설정
    def OpenWindow_SelectOne(self):
        # 창 설정
        win_select_1 = Tk()
        win_select_1.title("학기 선택")
        win_select_1.geometry("400x300")
        win_select_1.option_add("*Font", "맑은고딕 25")
        
        # 하위 컴포넌트 선언
        # Button: 학기 수 만큼
        # Label: 1
        label_select_1 = Label(win_select_1)
        button_select_1 = [Button(win_select_1) for _ in range(self.cnt_seme)]
        
        # 라벨 설정
        label_select_1.config(text = "한 개의 학기를 선택하세요.")
        
        # 버튼 설정
        for i in range(self.cnt_seme):
            button_select_1[i].config(text = self.seme_list[i]
                                        ,command = partial(self.OpenWindow_OneSemesterAnalysis, i))
            
        # 출력
        label_select_1.pack()
        for i in range(self.cnt_seme):
            button_select_1[i].pack()
        win_select_1.mainloop()

    def OpenWindow_OneSemesterAnalysis(self,semster):
        # 창 설정
        win_func_1 = Tk()
        win_func_1.title("한 학기 분석")
        win_func_1.geometry("400x300")
        win_func_1.option_add("*Font", "맑은고딕 25")
        # 하위 컴포넌트 선언
        # Label : 2
        label_func_1 = [Label(win_func_1) for _ in range(3)]
        
        # 라벨 설정
        label_func_1[1].config(text= "한 학기 분석")
        label_func_1[1].config(text= str(self.seme_list[semster]))
        label_func_1[2].config(text= str(self.user_info[self.seme_list[semster]]))
        
        for i in range(3):
            label_func_1[i].pack()

    
    # 두번째 기능 선택 이벤트 핸들러
    def OpenWindow_SelectTwo(self):
        # 창 설정
        win_select_two = Tk()
        win_select_two.title("비교 학기 선택창")
        win_select_two.geometry("650x400")
        win_select_two.resizable(width = FALSE, height = FALSE)

        # 하위 컴포넌트 선언
        # Button : 1
        # Combobox : 2
        button_select_two = Button(win_select_two)
        self.combobox_1 = ttk.Combobox(win_select_two)
        self.combobox_2 = ttk.Combobox(win_select_two)
        
        #비교 학기 선택창에 콤보박스 생성
        self.combobox_1.config(height = 20)
        self.combobox_1.config(value = self.seme_list)
        self.combobox_1.current(0)

        self.combobox_2.config(height = 20)
        self.combobox_2.config(value = self.seme_list)
        self.combobox_2.current(0)
        button_select_two.config(command = self.OpenWindow_TwoSemesterCompare)
        
        
        #출력
        self.combobox_1.pack()
        self.combobox_2.pack()
        button_select_two.pack()
        
        win_select_two.mainloop()
        
    def OpenWindow_TwoSemesterCompare(self):
        list_1 = self.user_info[self.combobox_1.get()]
        list_2 = self.user_info[self.combobox_2.get()]
        
        print(list_1)
        print(list_2)
        print()
        
    # 세번째 기능 선택 이벤트 핸들러
    def FuncEventHandler3(self):
        self.win_sem3 = Tk()
        self.win_sem3.title("Klas semester3")
        self.win_sem3.geometry("400x300")
        self.win_sem3.option_add("*Font", "맑은고딕 25")
        idx = len(self.sem_list)-1
        self.label1 = Label(self.win_sem3, text = self.sem_list[idx] + "학기 학점 결과보기")
        self.label1.pack()
        
class SubBoxManager():
    def __init__(self):
        print()
    def MessageBox(self,string):
        self.win_message = Tk()
        self.win_message.title("Message")
        self.win_message.geometry("384x128")
        self.win_message.option_add("*Font", "맑은고딕 12")
        
        label_message = Label(master=self.win_message)
        button_message = Button(master=self.win_message)
        
        label_message.config(text = string,justify= CENTER, wraplength= 300)
        button_message.config(text="확인",command=self.Check_Ok)
        
        label_message.pack(expand=True, fill="both")
        button_message.pack(side="bottom", anchor="s",pady=10)
        self.win_message.mainloop()
    
    def LoadingBox(self):
        self.win_loading = Tk()
        self.win_loading.title("Loading")
        self.win_loading.geometry("384x128")
        self.win_loading.option_add("*Font", "맑은고딕 12")
        
        Label(self.win_loading,text="Klas에서 정보를 가져오고 있습니다..").pack(fill="both",pady=10)
        Label(self.win_loading,text="( 최대 소요시간: 5분 )").pack(fill="both")
        
        progress = ttk.Progressbar(self.win_loading,orient=HORIZONTAL,length=300,mode='determinate')
        progress.pack(pady=10)
        progress.start(10)
        self.win_loading.mainloop()
        
    def Check_Ok(self):
        self.win_message.destroy()