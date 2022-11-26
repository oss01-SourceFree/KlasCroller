from tkinter import *
from tkinter import ttk

import os
import sys
import tkinter.font

import webbrowser

from math import pi

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.rcParams['font.family']='NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

from caching import CacheManager

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
    def __init__(self, user_info = {}, id = ''):
        self.id = id
        self.pw = ''
        
        self.category = ['의지력', '사고력' , '생존력' , '근면성' , '가성비']
        # 유저 정보 ( 의지력 , 사고력 , 생존력 , 근명성 , 가성비)
        self.user_info = user_info
        self.user_copy = user_info
        # 전체(완료+현재) 학기 이름 (ex) 2022년 1학기)
        self.seme_list = list(user_info.keys())
        # 전체(완료+현재) 학기 수
        self.cnt_seme = len(user_info)
        
        # 계정을 삭제하고 종료하는지, 계정을 저장한 상태로 종료하는지
        self.close_type = 0
        
        
    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
        
        # 창 설정
        self.win_lo = Tk()
        self.win_lo.title("Klas Log-in")
        self.win_lo.geometry("400x500-100+50")
        
        self.win_lo.protocol("WM_DELETE_WINDOW", self.CloseWindow_Login)
        
        # 폰트들 설정
        self.font1=tkinter.font.Font(family="나눔스퀘어라운드 ExtraBold", size=20, weight="bold")
        self.font2=tkinter.font.Font(family="나눔스퀘어라운드 ExtraBold", size=10, weight="bold")  
        
        self.can_1 = Canvas(self.win_lo, width=400, height=500, background='#7C1B0F', highlightthickness = 0)
        self.can_1.pack(padx=0, pady=0)
        self.can_1.place(x=0, y=0)

        self.can_2 = Canvas(self.win_lo, width=300, height=85, background='#7C1B0F')
        self.can_2.pack(padx=0, pady=0)
        self.can_2.place(x=50, y=55)

        # 배경 이미지
        img = PhotoImage(file=resource_path("KlasCroller\\img\\back.png"))
        self.can_1.create_image(200, 250, image=img)

        file_img2 = resource_path("KlasCroller\\img\\campus_logo.png")
        img2 = PhotoImage(file=file_img2)
        self.can_2.create_image(157, 45, image=img2)

        # id 입력창
        self.ent1 = Entry(self.win_lo, relief="groove")
        self.ent1.insert(0, "ID : 학번을 입력하세요")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.ent1.get() == "ID : 학번을 입력하세요":
                self.ent1.delete(0, len(self.ent1.get()))
        self.ent1.bind("<Button-1>", clear)
        self.ent1.place(x=50,y=200,width=300,height=35)

        # pw 입력창
        self.ent2 = Entry(self.win_lo)
        self.ent2.config(show="*")
        self.ent2.place(x=50,y=270,width=300,height=35)
        
        btn = Button(self.win_lo, font=self.font2, bg="white", fg="black")
        btn.config(text = "로그인")
        btn.place(x=150,y=350,width=100,height=40)
        btn.config(command=self.EventHandler_Login)
        
        self.win_lo.mainloop()
        
    def CloseWindow_Login(self):
        self.win_lo.destroy()
        exit(0)
    
    def GetIdPw(self):
        self.OpenWindow_Login()
        return self.id,self.pw

    # 로그인 이벤트 핸들러
    def EventHandler_Login(self):
        self.id = self.ent1.get()
        self.pw = self.ent2.get()
        
        self.can_1.destroy()
        self.can_2.destroy()
        
        self.win_lo.destroy()
    
    def Run_Main(self):
        self.OpenWindow_MainMenu()
        path_user_file = resource_path("KlasCroller\\usr")
        CacheManager(path_user_file, self.id).DestoryFile()
        SubBoxManager().MessageBox("KlasCroller가 수집한\n 이용자님의 정보가 삭제되었습니다.")
            
        exit(0)
    
    # 메인메뉴 창 열기
    def OpenWindow_MainMenu(self):
        
        # 하나의 기능 창만 열릴 수 있도록
        # boolean 형 변수 초기화
        self.is_opend_win_func1 = False
        self.is_opend_win_func2 = False
        self.is_opend_win_func3 = False
        self.is_opend_win_func4 = False
        
        # 알림 창 선언
        self.win_notice_func1 = -1
        self.win_notice_func2 = -1
        self.win_notice_func3 = -1
        self.win_notice_func4 = -1
        
        # 하위 창 선언
        self.win_func1 = -1
        self.win_func2 = -1
        self.win_func3 = -1
        
        # 창 설정
        self.win_main = Tk()
        self.win_main.title("Main Menu")
        self.win_main.geometry("500x560-100+50") # 가로 세로
        self.win_main.resizable(True, True)
        
        self.win_main.protocol("WM_DELETE_WINDOW", self.CloseWindow_MainMenu)
        
        can = Canvas(self.win_main, width=500, height=230,background='red', highlightthickness = 0)
        can.pack(padx=0, pady=0)
        can.place(x=0, y=0)
        
        # 바탕 광운대 사진 삽입
        file_back = resource_path("KlasCroller\\img\\back.png")
        back = PhotoImage(file=file_back)
        can.create_image(0,0,image=back)

        # 각 기능 버튼에 해당하는 이미지들
        img1 = PhotoImage(file=resource_path("KlasCroller\img\img_analysis_black.png"))

        img2 = PhotoImage(file=resource_path("KlasCroller\img\img_compare_black.png"))

        img3 = PhotoImage(file=resource_path("KlasCroller\img\img_mbti_black.png"))

        img4 = PhotoImage(file=resource_path("KlasCroller\img\img_search_black.png"))
        
        # 폰트들 설정
        self.font0=tkinter.font.Font(family="나눔스퀘어라운드 ExtraBold", size=30, weight="bold")
        self.font1=tkinter.font.Font(family="나눔스퀘어라운드 ExtraBold", size=20, weight="bold")
        self.font2=tkinter.font.Font(family="나눔스퀘어라운드 ExtraBold", size=10, weight="bold")  

        lab1 = Label(self.win_main)
        lab1.config(text = "KlasCroller", font=self.font0, foreground='white', background='#7C1B0F')
        lab1.place(x=25,y=25)

        # 사용자 학번
        lab2 = Label(self.win_main)
        lab2.config(text = str(self.id) + " 님, 반갑습니다.", font=self.font1, foreground='white', background='#7C1B0F')
        lab2.place(x=25,y=170)

        b1 = Button(self.win_main, text = "단일 학기\n 분석",font=self.font2, bg="white", fg="black",image=img1, compound="left",command=self.OpenWindow_Notice_Function1)
        b2 = Button(self.win_main, text = "두개 학기\n 비교", font=self.font2, bg="white", fg="black",image=img2, compound="left",command=self.OpenWindow_Notice_Function2)
        b3 = Button(self.win_main, text = "SF\nMBTI", font=self.font2, bg="white", fg="black",image=img3, compound="left",command=self.OpenWindow_Notice_Function3)
        b4 = Button(self.win_main, text = "취업정보 확인", font=self.font2, bg="white", fg="black",image=img4, compound="left",command=self.OpenWindow_Notice_Function4)
        b1.place(x=0,y=220,width=250, height=170)
        b2.place(x=250,y=220,width=250, height=170)
        b3.place(x=0,y=390,width=250, height=170)
        b4.place(x=250,y=390,width=250, height=170);
        
        # 캐시파일 삭제
        Button(self.win_main,
            text="계정 초기화",
            bg='#7C1B0F',
            fg='snow',
            font=self.font2,
            command = self.Delete_userInfo
            ).place(x=400,y=20,width=95,height=25)
        
        self.win_main.mainloop()
    
    def Delete_userInfo(self):
        self.close_type = 1
        self.win_main.destroy()
        
    def CloseWindow_MainMenu(self):
        self.close_type = 0
        self.win_main.destroy()
        exit(0)
    
    # 첫번째 기능 알림 창 open
    def OpenWindow_Notice_Function1(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.win_notice_func1 = -1
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.win_notice_func2 = -1
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.win_notice_func3 = -1
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.win_notice_func4 = -1
            self.is_opend_win_func4 = False
            
        # func1 창이 열림
        self.is_opend_win_func1 = True
        
        # 하위 창 초기화
        if self.win_func1 != -1:
            self.win_func1.destroy()
            self.win_func1 = -1
        if self.win_func2 != -1:
            self.win_func2.destroy()
            self.win_func2 = -1
        if self.win_func3 != -1:
            self.win_func3.destroy()
            self.win_func3 = -1
        
        # 창 설정
        self.win_notice_func1 = Toplevel(self.win_main)
        self.win_notice_func1.title("한 한기 분석 알림")
        self.win_notice_func1.geometry("400x450+100+50")
        self.win_notice_func1.resizable(width = FALSE, height = FALSE)

        # 배경
        canvas = Canvas(self.win_notice_func1,
                        width=400,
                        height=450,
                        background='#7C1B0F',
                        highlightthickness = 0)
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)
        img1 = PhotoImage(file=resource_path("KlasCroller\\img\\back.png"))
        canvas.create_image(200, 230, image=img1)
        
        # 제목 옆에 이미지
        img2 = PhotoImage(file=resource_path("KlasCroller\\img\\img_analysis_white.png"))
        Label(self.win_notice_func1, image=img2, background='#7C1B0F').place(x=70, y=95)
        
        
        # 창 Title
        Label(master=self.win_notice_func1,text = "단일 학기 분석",
            font=self.font1,foreground='white',
            background='#7C1B0F',
            justify= CENTER).place(x=130,y=100)
        
        # 설명글
        Label(master=self.win_notice_func1,
            text = "아래의 드롭다운 메뉴에서\n\n분석하고 싶은 학기를 선택해주세요.\n\n\n 선택된 학기에 대해 \n\n오각 방사 그래프를 출력해드립니다.",
            font=self.font2,foreground='white', 
            background='#7C1B0F',
            justify= CENTER).place(x=95,y=150)
        
        # 비교 학기 선택창에 콤보박스 생성
        self.combobox_1_1 = ttk.Combobox(self.win_notice_func1)
        self.combobox_1_1.config(value = self.seme_list)
        self.combobox_1_1.current(0)
        self.combobox_1_1.place(x=70,y=300,width=260,height=30)
        
        
        # 분석하기 버튼
        Button(self.win_notice_func1,
            text="분석하기",
            bg='#7C1B0F',
            fg='snow',
            font=self.font2,
            command = self.OpenWindow_OneSemesterAnalysis).place(x=160,y=400,width=80,height=25)
        
        
        self.win_notice_func1.mainloop()
        
    def OpenWindow_OneSemesterAnalysis(self):
        self.sem = self.combobox_1_1.get()
        
        self.data_list = self.user_info[self.sem].copy()
        self.data_list += self.data_list[:1]
        
        angles = [n/float(5) * 2 *pi for n in range(5)]
        angles += angles[:1]
        
        fig,ax = plt.subplots(1,1,figsize=(3,5),subplot_kw=dict(polar=True))
        ax.patch.set_facecolor('#7C1B0F')
        fig.patch.set_facecolor('#7C1B0F')
        ax.set_theta_offset(pi / 2) ## 시작점
        ax.set_theta_direction(-1) ## 그려지는 방향 시계방향
        plt.title(self.sem, size=15, color='white')
        
        plt.xticks(angles[:-1],self.category,color='white',size=10)
        ax.tick_params(axis='x', which='major', pad=5)
        plt.yticks([20,40,60,80],['','','',''],color='white',size=10)
        plt.ylim(0,100)
        ax.set_rlabel_position(100)
        
        ax.plot(angles,self.data_list,linewidth=3,linestyle='solid',color='#FFFF00')
        ax.fill(angles,self.data_list,'#FFFF00',alpha=0.5) 
        
        self.win_func1 = Toplevel(self.win_notice_func1)
        self.win_func1.config(bg='#7C1B0F')
        self.win_func1.title(self.sem+" 학기 분석")
        self.win_func1.geometry("650x400+150+100")
        self.win_func1.resizable(width = FALSE, height = FALSE)
        
        parameter_label = [Label(self.win_func1) for _ in range(5)]
        value_label = [Label(self.win_func1) for _ in range(5)]

        
        for i in range(5):
            parameter_label[i].config(text = self.category[i], font = self.font1, bg='#69180D', fg = 'yellow')
            parameter_label[i].place(x=420, y= 20 + 80*i)
            
            value_label[i].config(text = self.user_info[self.sem][i], font = self.font1, bg='#69180D', fg = 'snow')
            value_label[i].place(x=550, y= 20 + 80*i)
        
        canvas = FigureCanvasTkAgg(fig, master=self.win_func1)
        canvas.get_tk_widget().pack(anchor='w')

    # 두번째 기능 알림 창 open
    def OpenWindow_Notice_Function2(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.win_notice_func1 = -1
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.win_notice_func2 = -1
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.win_notice_func3 = -1
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.win_notice_func4 = -1
            self.is_opend_win_func4 = False
            
        # func2 창이 열림
        self.is_opend_win_func2 = True
        
        # 하위 창 초기화
        if self.win_func1 != -1:
            self.win_func1.destroy()
            self.win_func1 = -1
        if self.win_func2 != -1:
            self.win_func2.destroy()
            self.win_func2 = -1
        if self.win_func3 != -1:
            self.win_func3.destroy()
            self.win_func3 = -1
        
        # 창 설정
        self.win_notice_func2 = Toplevel(self.win_main)
        self.win_notice_func2.title("두 학기 비교 알림")
        self.win_notice_func2.geometry("400x450+100+50")
        self.win_notice_func2.resizable(width = FALSE, height = FALSE)
        
        # 배경
        canvas = Canvas(self.win_notice_func2,
                        width=400,
                        height=450,
                        background='#7C1B0F',
                        highlightthickness = 0)
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)
        img1 = PhotoImage(file=resource_path("KlasCroller\\img\\back.png"))
        canvas.create_image(200, 230, image=img1)
        
        # 제목 옆에 이미지
        img2 = PhotoImage(file=resource_path("KlasCroller\\img\\img_compare_white.png"))
        Label(self.win_notice_func2, image=img2, background='#7C1B0F').place(x=70, y=95)
        
        # 창 Title
        Label(master=self.win_notice_func2,
            text = "두 개 학기 비교 ",
            font=self.font1,
            foreground='white',
            background='#7C1B0F',
            justify= CENTER).place(x=130,y=100)
        
        # 설명글
        Label(master=self.win_notice_func2,
            text = "아래의 드롭다운 메뉴에서\n\n비교하고 싶은 학기를 선택해주세요.\n\n\n 선택된 학기에 대해 \n\n막대 그래프를 출력해드립니다.",
            font=self.font2,foreground='white', 
            background='#7C1B0F',
            justify= CENTER).place(x=95,y=150)
        
        # 비교 학기 선택창에 콤보박스 생성
        self.combobox_2_1 = ttk.Combobox(self.win_notice_func2)
        self.combobox_2_2 = ttk.Combobox(self.win_notice_func2)
        
        self.combobox_2_1.config(value = self.seme_list)
        self.combobox_2_1.current(0)
        self.combobox_2_1.place(x=70,y=300,width=260,height=30)
        
        self.combobox_2_2.config(value = self.seme_list)
        self.combobox_2_2.current(0)
        self.combobox_2_2.place(x=70,y=350,width=260,height=30)
        
        # 비교하기 버튼
        Button(self.win_notice_func2,
            text="비교하기",
            bg='#7C1B0F',
            fg='snow',
            font=self.font2,
            command = self.OpenWindow_TwoSemesterCompare).place(x=160,y=400,width=80,height=25)
        
        self.win_notice_func2.mainloop()
        
    def OpenWindow_TwoSemesterCompare(self):
        self.sem1 = self.combobox_2_1.get()
        self.sem2 = self.combobox_2_2.get()
        self.list_1 = self.user_info[self.sem1].copy()
        self.list_2 = self.user_info[self.sem2].copy()
        
        x = np.arange(len(self.category))
        width = 0.3
            
        fig, ax =plt.subplots(figsize=(4,5))
        ax.patch.set_facecolor('#7C1B0F')
        fig.patch.set_facecolor('#7C1B0F')
        plt.bar(x, self.list_1, width, color='#FFFFFF',alpha = 0.5, edgecolor = '#FFFFFF', linewidth = 2)
        plt.bar(x + width+0.1, self.list_2, width, color='#FFFF00',alpha = 0.5, edgecolor = '#FFFF00', linewidth = 2)
        plt.xticks(x+width, self.category, color ='white')
        plt.yticks(color='white')
        
        plt.title(self.sem1+' vs '+self.sem2,color='white')
        
        self.win_func2 = Toplevel(self.win_notice_func2)
        self.win_func2.config(bg='#7C1B0F')
        self.win_func2.title(self.sem1+','+self.sem2+" 학기 비교")
        self.win_func2.geometry("650x400+150+100")
        self.win_func2.resizable(width = FALSE, height = FALSE)
        
        
        
        
        parameter_label = [Label(self.win_func2) for _ in range(5)]
        # seme_1_label = [Label(window_func_2) for _ in range(5)]
        # seme_1_label = [Label(window_func_2) for _ in range(5)]
        value_1_label = [Label(self.win_func2) for _ in range(5)]
        value_2_label = [Label(self.win_func2) for _ in range(5)]
        
        for i in range(5):
            parameter_label[i].config(text = self.category[i], font = self.font1, bg='snow', fg = 'black')
            parameter_label[i].place(x=420, y= 22 + 80*i)
            
            string_1 = self.sem1+"   "+str(self.list_1[i])
            value_1_label[i].config(text = string_1, font = self.font2, bg='#69180D', fg = 'snow')
            value_1_label[i].place(x=505, y= 15 + 80*i)
            
            string_2 = self.sem2+"   "+ str(self.list_2[i])
            value_2_label[i].config(text = string_2, font = self.font2, bg='#69180D', fg = 'yellow')
            value_2_label[i].place(x=505, y= 40 + 80*i)
        canvas = FigureCanvasTkAgg(fig, master=self.win_func2)
        canvas.get_tk_widget().pack(anchor='w')
        
        
        
        
        
    # 세번째 기능 알림 창 open
    def OpenWindow_Notice_Function3(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.win_notice_func1 = -1
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.win_notice_func2 = -1
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.win_notice_func3 = -1
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.win_notice_func4 = -1
            self.is_opend_win_func4 = False
            
        # func3 창이 열림
        self.is_opend_win_func3 = True
        
        # 하위 창 초기화
        if self.win_func1 != -1:
            self.win_func1.destroy()
            self.win_func1 = -1
        if self.win_func2 != -1:
            self.win_func2.destroy()
            self.win_func2 = -1
        if self.win_func3 != -1:
            self.win_func3.destroy()
            self.win_func3 = -1
        
        # 창 설정
        self.win_notice_func3 = Toplevel(self.win_main)
        self.win_notice_func3.title("학업 스타일 분석")
        self.win_notice_func3.geometry("400x450+100+50")
        self.win_notice_func3.resizable(width = FALSE, height = FALSE)
        
        # 배경
        canvas = Canvas(self.win_notice_func3,
                        width=400,
                        height=450,
                        background='#7C1B0F',
                        highlightthickness = 0)
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)
        img1 = PhotoImage(file=resource_path("KlasCroller\\img\\back.png"))
        canvas.create_image(200, 230, image=img1)
        
        # 제목 옆에 이미지
        img2 = PhotoImage(file=resource_path("KlasCroller\\img\\img_mbti_white.png"))
        Label(self.win_notice_func3, image=img2, background='#7C1B0F').place(x=80, y=85)
        
        # 창 Title
        Label(master=self.win_notice_func3,
            text = "SF MBTI",
            font=self.font1,
            foreground='white',
            background='#7C1B0F',
            justify= CENTER).place(x=140,y=100)

        # 설명글
        Label(master=self.win_notice_func3,
            text = " 지난 학기동안 당신은 어떻게\n\n학업을 수행하셨을까요?\n\n\n당신의 학업 성취 스타일과 맞는\n\n동물 사진을 출력해드립니다.",
            font=self.font2,
            foreground='white', 
            background='#7C1B0F',
            justify= CENTER).place(x=95,y=150)
        
        # 확인하기 버튼
        Button(self.win_notice_func3,
            text="확인하기",
            bg='#7C1B0F',
            fg='snow',
            font=self.font2,
            command = self.OpenWindow_PrintUserStyle).place(x=150,y=300,width=80,height=25)
        
        self.win_notice_func3.mainloop()
        
    def OpenWindow_PrintUserStyle(self):
        
        self.win_func3 = Toplevel(self.win_notice_func3)
        self.win_func3.config(bg='#7C1B0F')
        self.win_func3.title('SF MBTI')
        self.win_func3.geometry("650x400+150+100")
        self.win_func3.resizable(width = FALSE, height = FALSE)
        
        Label(self.win_func3,text="학업 스타일 분석",font=self.font1,bg='#7C1B0F',fg='snow').place(x=220,y=10)
        
        
        
        # 사용자 style 뽑아내는 로직
        good_adjective_list = ['열정많은','저명한','끈질긴','부지런한','운 좋은']
        good_noun_list = ['소나무','돌고래','쥐','개미','네잎클로버']

        bad_adjective_list = ['노력상실','우둔한','포기빠른','게으른','불운한']
        bad_noun_list = ['베짱이','금붕어','게복치','나무늘보','까마귀']
        
        good_back_imgs = ['KlasCroller\\img\\back_p_1.png',
                    'KlasCroller\\img\\back_p_2.png',
                    'KlasCroller\\img\\back_p_3.png',
                    'KlasCroller\\img\\back_p_4.png',
                    'KlasCroller\\img\\back_p_5.png']
        bad_back_imgs = ['KlasCroller\\img\\back_n_1.png',
                    'KlasCroller\\img\\back_n_2.png',
                    'KlasCroller\\img\\back_n_3.png',
                    'KlasCroller\\img\\back_n_4.png',
                    'KlasCroller\\img\\back_n_5.png']
        
        good_ani_imgs = ['KlasCroller\\img\\img_p_1.png',
                    'KlasCroller\\img\\img_p_2.png',
                    'KlasCroller\\img\\img_p_3.png',
                    'KlasCroller\\img\\img_p_4.png',
                    'KlasCroller\\img\\img_p_5.png']
        bad_ani_imgs = ['KlasCroller\\img\\img_n_1.png',
                    'KlasCroller\\img\\img_n_2.png',
                    'KlasCroller\\img\\img_n_3.png',
                    'KlasCroller\\img\\img_n_4.png',
                    'KlasCroller\\img\\img_n_5.png']
        
        list_a =[]  # 의지력 list
        list_b =[]  # 사고력 list
        list_c =[]  # 생존력 list
        list_d =[]  # 근면성 list
        list_e =[]  # 가성비 list


        for seme in self.seme_list:
            list_a.append(self.user_info[seme][0])
            list_b.append(self.user_info[seme][1])
            list_c.append(self.user_info[seme][2])
            list_d.append(self.user_info[seme][3])
            list_e.append(self.user_info[seme][4])

        list_median = []
        list_median.append(np.median(list_a))
        list_median.append(np.median(list_b))
        list_median.append(np.median(list_c))
        list_median.append(np.median(list_d))
        list_median.append(np.median(list_e))
        del list_a, list_b, list_c, list_d, list_e

        # (best, second_best): list_median에서 최고, 차고 값의 인덱스
        # (worst, second_worst): list_median에서 최저, 차저 값의 인덱스
        best = second_best = worst = second_worst = 0
        # tmp: 차고, 차저 값의 인덱스 추출시 최고,최저 값을 잠시 저장하기 위해 쓰는 변수
        tmp = 0

        # (best, second_best): list_median에서 최고, 차고 값의 인덱스
        best = list_median.index(max(list_median))
        tmp = list_median[best]
        list_median[best] = -1
        second_best = list_median.index(max(list_median))
        list_median[best] = tmp

        # (worst, second_worst): list_median에서 최저, 차저 값의 인덱스
        worst = list_median.index(min(list_median))
        tmp = list_median[worst]
        list_median[worst] = 101
        second_worst = list_median.index(min(list_median))
        list_median[worst] = tmp
        del list_median

        str_good = good_adjective_list[second_best] +' '+ good_noun_list[best]
        str_bad = bad_adjective_list[second_worst] +' '+ bad_noun_list[worst]
        
        
        img1 = PhotoImage(file=resource_path("KlasCroller\\img\\img_board.png"))
        
        canvas_card1 = Canvas(self.win_func3, width=246, height=328,background='#7C1B0F', highlightthickness = 0)
        canvas_card1.place(x=50, y=65)
        canvas_card1.create_image(123, 164, image=img1)
        
        canvas_card2 = Canvas(self.win_func3, width=246, height=328,background='#7C1B0F', highlightthickness = 0)
        canvas_card2.place(x=365, y=65)
        canvas_card2.create_image(123, 164, image=img1)
        
        canvas_pos_animal = Canvas(self.win_func3, width=185, height=185 ,background='white', highlightthickness = 0)
        canvas_pos_animal.place(x=80, y=185)
        background_img_1 =  PhotoImage(file=resource_path(good_back_imgs[second_best]))
        foreground_img_1 =  PhotoImage(file=resource_path(good_ani_imgs[best]))
        canvas_pos_animal.create_image(185//2,185//2,image=background_img_1)
        canvas_pos_animal.create_image(185//2,185//2,image=foreground_img_1)
        
        canvas_neg_animal = Canvas(self.win_func3, width=185, height=185 ,background='white', highlightthickness = 0)
        canvas_neg_animal.place(x=396, y=185)
        background_img_2 =  PhotoImage(file=resource_path(bad_back_imgs[second_worst]))
        foreground_img_2 =  PhotoImage(file=resource_path(bad_ani_imgs[worst]))
        canvas_neg_animal.create_image(185//2,185//2,image=background_img_2)
        canvas_neg_animal.create_image(185//2,185//2,image=foreground_img_2)
        
        Label(self.win_func3,text=str_good,font=self.font2,bg='white',fg='black').place(x=80,y=125)
        Label(self.win_func3,text="- "+self.category[best] + " 이/가 제일 훌륭합니다.",font=self.font2,bg='white',fg='black').place(x=80,y=145)
        Label(self.win_func3,text="- "+self.category[second_best] + " 이/가 뛰어납니다.",font=self.font2,bg='white',fg='black').place(x=80,y=165)
        
        Label(self.win_func3,text=str_bad ,font=self.font2,bg='white',fg='black').place(x=395,y=125)
        Label(self.win_func3,text="- "+self.category[worst] + " 이/가 제일 필요합니다.",font=self.font2,bg='white',fg='black').place(x=395,y=145)
        Label(self.win_func3,text="- "+self.category[second_worst] + " 이/가 부족합니다.",font=self.font2,bg='white',fg='black').place(x=395,y=165)
        
        
        self.win_func3.mainloop()
        
        
        
        
        
        
        
        
# 네번째 기능 알림 창 open
    def OpenWindow_Notice_Function4(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.win_notice_func1 = -1
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.win_notice_func2 = -1
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.win_notice_func3 = -1
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.win_notice_func4 = -1
            self.is_opend_win_func4 = False
            
        # func4 창이 열림
        self.is_opend_win_func4 = True
        
        # 창 설정
        self.win_notice_func4 = Toplevel(self.win_main)
        self.win_notice_func4.title("학업 스타일 분석")
        self.win_notice_func4.geometry("400x450+100+50")
        self.win_notice_func4.resizable(width = FALSE, height = FALSE)
        
        # 배경
        canvas = Canvas(self.win_notice_func4,
                        width=400,
                        height=450,
                        background='#7C1B0F',
                        highlightthickness = 0)
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)
        img1 = PhotoImage(file=resource_path("KlasCroller\\img\\back.png"))
        canvas.create_image(200, 230, image=img1)
        
        # 제목 옆에 이미지
        img2 = PhotoImage(file=resource_path("KlasCroller\\img\\img_search_white.png"))
        Label(self.win_notice_func4, image=img2, background='#7C1B0F').place(x=80, y=85)
        
        # 창 Title
        Label(master=self.win_notice_func4,
            text = "취업 공고 분야",
            font=self.font1,
            foreground='white',
            background='#7C1B0F',
            justify= CENTER).place(x=140,y=100)

        # 설명글
        Label(master=self.win_notice_func4,
            text = "\n\n입력하신 분야/직업\n\n잡코리아 취업공고가 출력됩니다.",
            font=self.font2,
            foreground='white', 
            background='#7C1B0F',
            justify= CENTER).place(x=95,y=150)
        
        # 입력창
        self.entry_search = Entry(master=self.win_notice_func4, relief = "groove")
        self.entry_search.insert(0,"예: 웹 개발, 앱 개발 ..")
        def clear(event):
            # 좌클릭 했을 때 입력차의 내용 다 지우기
            if self.entry_search.get() == "예: 웹 개발, 앱 개발 ..":
                self.entry_search.delete(0,len(self.entry_search.get()))
        self.entry_search.bind("<Button-1>",clear)
        self.entry_search.place(x=85,y=300,width=210,height=40)
        
        # 검색하기 버튼
        Button(self.win_notice_func4,
            text="검색하기",
            bg='#7C1B0F',
            fg='snow',
            font=self.font2,
            command = self.OpenWebsite).place(x=150,y=360,width=80,height=25)
        
        self.win_notice_func4.mainloop()
        
    def OpenWebsite(self):
        keyword = self.entry_search.get()
        url = 'https://www.jobkorea.co.kr/Search/?stext={}&tabType=recruit&Page_No=1'.format(keyword)
        webbrowser.open(url)
        
        
class SubBoxManager():
    def __init__(self):
        print()
    def __del__(self):
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
    
    def LoadingBox(self ,str="...", max_min = "5"):
        self.win_loading = Tk()
        self.win_loading.title("Loading")
        self.win_loading.geometry("384x128")
        self.win_loading.option_add("*Font", "맑은고딕 12")
        
        Label(self.win_loading,text=str).pack(fill="both",pady=10)
        Label(self.win_loading,text="( 최대 소요시간: "+max_min+"분 )").pack(fill="both")
        
        progress = ttk.Progressbar(self.win_loading,orient=HORIZONTAL,length=300,mode='determinate')
        progress.pack(pady=10)
        progress.start(10)
        self.win_loading.mainloop()
        
    def Check_Ok(self):
        self.win_message.destroy()
        