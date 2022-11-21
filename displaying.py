from tkinter import *
from tkinter import ttk

import os
import sys
from functools import partial
import tkinter.font

from math import pi

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

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
        
        self.category = ['의지력', '지 능' , '생존력' , '근명성' , '가성비']
        # 유저 정보 ( 의지력 , 지능 , 생존력 , 근명성 , 가성비)
        self.user_info = user_info
        # 전체(완료+현재) 학기 이름 (ex) 2022년 1학기)
        self.seme_list = list(user_info.keys())
        # 전체(완료+현재) 학기 수
        self.cnt_seme = len(user_info)
        
        # 하나의 기능 창만 열릴 수 있도록
        # boolean 형 변수 초기화
        self.is_opend_win_func1 = False
        self.is_opend_win_func2 = False
        self.is_opend_win_func3 = False
        self.is_opend_win_func4 = False
        
    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
        # 창 설정
        self.win_lo = Tk()
        self.win_lo.title("Klas Log-in")
        self.win_lo.geometry("400x500")
        
        # self.win_lo.protocol('WM_DELETE_WINDOW',self.Exit_Window_Login_x)
        
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        
        self.can_1 = Canvas(self.win_lo, width=400, height=500, background='#7C1B0F')
        self.can_1.pack(padx=0, pady=0)
        self.can_1.place(x=0, y=0)

        self.can_2 = Canvas(self.win_lo, width=300, height=85, background='#7C1B0F')
        self.can_2.pack(padx=0, pady=0)
        self.can_2.place(x=50, y=55)

        file_img1 = resource_path("KlasCroller\\img\\back.png")
        img1 = PhotoImage(file=file_img1)
        self.can_1.create_image(200, 250, image=img1)

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
        
        btn = Button(self.win_lo, font=font, bg="white", fg="black")
        btn.config(text = "로그인")
        btn.place(x=150,y=350,width=100,height=40)
        btn.config(command=self.EventHandler_Login)
        
        self.win_lo.mainloop()
    
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
        
    # 메인메뉴 창 열기
    def OpenWindow_MainMenu(self):
        # 창 설정
        self.win_main = Tk()
        self.win_main.title("Main Menu")
        self.win_main.geometry("500x560") # 가로 세로
        self.win_main.resizable(True, True)
        
        self.win_main.protocol('WM_DELETE_WINDOW',self.win_main.iconify)
        self.win_main.bind('<Escape>', lambda e: self.win_main.destroy())
        
        # 폰트들 설정
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        font1=tkinter.font.Font(family="휴먼둥근헤드라인", size=30)#, weight="bold")
        font2=tkinter.font.Font(family="휴먼둥근헤드라인", size=17)
        
        can = Canvas(self.win_main, width=500, height=230,background='red')
        can.pack(padx=0, pady=0)
        can.place(x=0, y=0)
        
        # 바탕 광운대 사진 삽입
        file_back = resource_path("KlasCroller\\img\\back.png")
        back = PhotoImage(file=file_back)
        can.create_image(0,0,image=back)

        # 각 기능 버튼에 해당하는 이미지들
        file_img1 = resource_path("KlasCroller\img\img1.png")
        img1 = PhotoImage(file=file_img1)

        file_img2 = resource_path("KlasCroller\img\img2.png")
        img2 = PhotoImage(file=file_img2)

        file_img3 = resource_path("KlasCroller\img\img3.png")
        img3 = PhotoImage(file=file_img3)

        file_img4 = resource_path("KlasCroller\img\img4.png")
        img4 = PhotoImage(file=file_img4)

        lab1 = Label(self.win_main)
        lab1.config(text = "기능선택", font=font1, foreground='white', background='#7C1B0F')
        lab1.place(x=25,y=25)

        # 사용자 이름(사용자 이름 크롤링 활용해야해요!)
        lab2 = Label(self.win_main)
        lab2.config(text = str(self.id) + " 님, 반갑습니다.", font=font2, foreground='white', background='#7C1B0F')
        lab2.place(x=25,y=170)

        b1 = Button(self.win_main, text = "단일 학기\n 분석",font=font, bg="white", fg="black",image=img1, compound="left",command=self.OpenWindow_Notice_Function1)
        b2 = Button(self.win_main, text = "두개 학기\n 비교", font=font, bg="white", fg="black",image=img2, compound="left",command=self.OpenWindow_Notice_Function2)
        b3 = Button(self.win_main, text = "SF\nMBTI", font=font, bg="white", fg="black",image=img3, compound="left",command=self.OpenWindow_Notice_Function3)
        b4 = Button(self.win_main, text = "취업정보 확인", font=font, bg="white", fg="black",image=img4, compound="left")
        b1.place(x=0,y=220,width=250, height=170)
        b2.place(x=250,y=220,width=250, height=170)
        b3.place(x=0,y=390,width=250, height=170)
        b4.place(x=250,y=390,width=250, height=170);
        self.win_main.mainloop()
    
    
    
    # 첫번째 기능 알림 창 open
    def OpenWindow_Notice_Function1(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.is_opend_win_func4 = False
            
        # func1 창이 열림
        self.is_opend_win_func1 = True
            
        # 폰트들 설정
        font1=tkinter.font.Font(family="휴먼둥근헤드라인", size=20)
        
        # 창 설정
        self.win_notice_func1 = Toplevel(self.win_main)
        self.win_notice_func1.title("학기 선택창")
        self.win_notice_func1.geometry("400x450")
        self.win_notice_func1.resizable(width = FALSE, height = FALSE)
        
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        
        canvas = Canvas(self.win_notice_func1, width=400, height=450, background='#7C1B0F')
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)

        file_img1 = resource_path("KlasCroller\\img\\back.png")
        img1 = PhotoImage(file=file_img1)
        canvas.create_image(200, 250, image=img1)
        
        
        label_title = Label(master=self.win_notice_func1)
        label_title.config(text = "[단일 학기 분석]",font=font1,foreground='white', background='#7C1B0F',justify= CENTER)
        label_title.place(x=95,y=100)
        
        label_content = Label(master=self.win_notice_func1)
        label_content.config(text = "아래의 드롭다운 메뉴에서\n\n분석하고 싶은 학기를 선택해주세요.\n\n\n 선택된 학기에 대해 \n\n오각 방사 그래프를 출력해드립니다.",font=font,foreground='white', background='#7C1B0F',justify= CENTER)
        label_content.place(x=95,y=150)
        
        # 비교 학기 선택창에 콤보박스 생성
        self.combobox_1_1 = ttk.Combobox(self.win_notice_func1)
        
        self.combobox_1_1.config(value = self.seme_list)
        self.combobox_1_1.current(0)
        self.combobox_1_1.place(x=70,y=300,width=260,height=30)
        
        button_select_1 = Button(self.win_notice_func1)
        button_select_1.config(text="분석",bg='#7C1B0F',fg='snow',font=font,command = self.OpenWindow_OneSemesterAnalysis)
        button_select_1.place(x=160,y=350,width=80,height=25)
        
        self.win_notice_func1.mainloop()
        
    def OpenWindow_OneSemesterAnalysis(self):
        title = self.combobox_1_1.get()
        data_list = self.user_info[title]
        data_list += data_list[:1]
        
        angles = [n/float(5) * 2 *pi for n in range(5)]
        angles += angles[:1]
        
        fig,ax = plt.subplots(1,1,figsize=(3,5),subplot_kw=dict(polar=True))
        ax.patch.set_facecolor('#7C1B0F')
        fig.patch.set_facecolor('#7C1B0F')
        ax.set_theta_offset(pi / 2) ## 시작점
        ax.set_theta_direction(-1) ## 그려지는 방향 시계방향
        plt.title(title, size=15, color='white')
        
        plt.xticks(angles[:-1],self.category,color='white',size=10)
        ax.tick_params(axis='x', which='major', pad=5)
        plt.yticks([20,40,60,80],['','','',''],color='white',size=10)
        plt.ylim(0,100)
        ax.set_rlabel_position(100)
        
        ax.plot(angles,data_list,linewidth=3,linestyle='solid',color='#FFFF00')
        ax.fill(angles,data_list,'#FFFF00',alpha=0.5) 
        
        window = Toplevel(self.win_notice_func1)
        window.config(bg='#7C1B0F')
        window.title(str(title)+" 학기 분석")
        window.geometry("650x400")
        window.resizable(width = FALSE, height = FALSE)
        
        parameter_label = [Label(window) for _ in range(5)]
        value_label = [Label(window) for _ in range(5)]
        
        font1=tkinter.font.Font(family="Malgun Gothic", size=22)
        font2=tkinter.font.Font(family="Malgun Gothic", size=18)
        
        for i in range(5):
            parameter_label[i].config(text = self.category[i], font = font1, bg='#69180D', fg = 'yellow')
            parameter_label[i].place(x=400, y= 20 + 80*i)
            
            value_label[i].config(text = self.user_info[title][i], font = font2, bg='#69180D', fg = 'snow')
            value_label[i].place(x=550, y= 20 + 80*i)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack(anchor='w')











    # 두번째 기능 알림 창 open
    def OpenWindow_Notice_Function2(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.is_opend_win_func4 = False
            
        # func2 창이 열림
        self.is_opend_win_func2 = True
        
        if self.win_notice_func1 != -1:
            self.win_notice_func1.destroy()
            self.win_notice_func1 = -1
        # 폰트들 설정
        font1=tkinter.font.Font(family="휴먼둥근헤드라인", size=20)
        
        # 창 설정
        self.win_notice_func2 = Toplevel(self.win_main)
        self.win_notice_func2.title("학기 선택창")
        self.win_notice_func2.geometry("400x450")
        self.win_notice_func2.resizable(width = FALSE, height = FALSE)
        
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        
        canvas = Canvas(self.win_notice_func2, width=400, height=450, background='#7C1B0F')
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)

        file_img1 = resource_path("KlasCroller\\img\\back.png")
        img1 = PhotoImage(file=file_img1)
        canvas.create_image(200, 250, image=img1)
        
        
        label_title = Label(master=self.win_notice_func2)
        label_title.config(text = "[두 개 학기 비교]",font=font1,foreground='white', background='#7C1B0F',justify= CENTER)
        label_title.place(x=90,y=100)
        
        label_content = Label(master=self.win_notice_func2)
        label_content.config(
            text = "아래의 드롭다운 메뉴에서\n\n비교하고 싶은 학기를 선택해주세요.\n\n\n 선택된 학기에 대해 \n\n막대 그래프를 출력해드립니다.",
            font=font,
            foreground='white',
            background='#7C1B0F',
            justify= CENTER)
        label_content.place(x=95,y=150)
    
        # 하위 컴포넌트 선언
        # Button : 1
        # Combobox : 2
        
        # 비교 학기 선택창에 콤보박스 생성
        self.combobox_2_1 = ttk.Combobox(self.win_notice_func2)
        self.combobox_2_2 = ttk.Combobox(self.win_notice_func2)
        
        self.combobox_2_1.config(value = self.seme_list)
        self.combobox_2_1.current(0)
        self.combobox_2_1.place(x=70,y=300,width=260,height=30)
        
        self.combobox_2_2.config(value = self.seme_list)
        self.combobox_2_2.current(0)
        self.combobox_2_2.place(x=70,y=350,width=260,height=30)
        
        button_select_2 = Button(self.win_notice_func2)
        button_select_2.config(text="분석",bg='#7C1B0F',fg='snow',font=font,command = self.OpenWindow_TwoSemesterCompare)
        button_select_2.place(x=160,y=400,width=80,height=25)
        
        self.win_notice_func2.mainloop()
        
    def OpenWindow_TwoSemesterCompare(self):
        sem1 = self.combobox_2_1.get()
        sem2 = self.combobox_2_2.get()
        list_1 = self.user_info[sem1]
        list_2 = self.user_info[sem2]
        
        x = np.arange(len(self.category))
        width = 0.3
            
        fig, ax =plt.subplots(figsize=(4,5))
        ax.patch.set_facecolor('#7C1B0F')
        fig.patch.set_facecolor('#7C1B0F')
        plt.bar(x, list_1, width, color='#FFFFFF',alpha = 0.5, edgecolor = '#FFFFFF', linewidth = 2)
        plt.bar(x + width+0.1, list_2, width, color='#FFFF00',alpha = 0.5, edgecolor = '#FFFF00', linewidth = 2)
        plt.xticks(x+width, self.category, color ='white')
        plt.yticks(color='white')
        
        plt.title(sem1+' vs '+sem2,color='white')
        
        window_func_2 = Toplevel(self.win_notice_func2)
        window_func_2.config(bg='#7C1B0F')
        window_func_2.title(sem1+','+sem2+" 학기 비교")
        window_func_2.geometry("650x400")
        window_func_2.resizable(width = FALSE, height = FALSE)
        
        
        
        
        parameter_label = [Label(window_func_2) for _ in range(5)]
        # seme_1_label = [Label(window_func_2) for _ in range(5)]
        # seme_1_label = [Label(window_func_2) for _ in range(5)]
        value_1_label = [Label(window_func_2) for _ in range(5)]
        value_2_label = [Label(window_func_2) for _ in range(5)]
        
        
        font1=tkinter.font.Font(family="Malgun Gothic", size=18)
        font2=tkinter.font.Font(family="Malgun Gothic", size=10)
        
        for i in range(5):
            parameter_label[i].config(text = self.category[i], font = font1, bg='snow', fg = 'black')
            parameter_label[i].place(x=420, y= 22 + 80*i)
            
            string_1 = sem1+"   "+str(list_1[i])
            value_1_label[i].config(text = string_1, font = font2, bg='#69180D', fg = 'snow')
            value_1_label[i].place(x=505, y= 8 + 80*i)
            
            string_2 = sem2+"   "+ str(list_2[i])
            value_2_label[i].config(text = string_2, font = font2, bg='#69180D', fg = 'yellow')
            value_2_label[i].place(x=505, y= 40 + 80*i)
        canvas = FigureCanvasTkAgg(fig, master=window_func_2)
        canvas.get_tk_widget().pack(anchor='w')
        
        
        
        
        
        
        
    # 세번째 기능 알림 창 open
    def OpenWindow_Notice_Function3(self):
        # main 창 제외하고 열린 창은 모두 닫기
        if self.is_opend_win_func1 :
            self.win_notice_func1.destroy()
            self.is_opend_win_func1 = False
        if self.is_opend_win_func2 :
            self.win_notice_func2.destroy()
            self.is_opend_win_func2 = False
        if self.is_opend_win_func3 :
            self.win_notice_func3.destroy()
            self.is_opend_win_func3 = False
        if self.is_opend_win_func4 :
            self.win_notice_func4.destroy()
            self.is_opend_win_func4 = False
            
        # func3 창이 열림
        self.is_opend_win_func3 = True
            
        # 폰트들 설정
        font=tkinter.font.Font(family="맑은 고딕 25", size=10, weight="bold")
        font1=tkinter.font.Font(family="휴먼둥근헤드라인", size=20)
        
        # 창 설정
        self.win_notice_func3 = Toplevel(self.win_main)
        self.win_notice_func3.title("학기 선택창")
        self.win_notice_func3.geometry("400x450")
        self.win_notice_func3.resizable(width = FALSE, height = FALSE)
        
        canvas = Canvas(self.win_notice_func3, width=400, height=450, background='#7C1B0F')
        canvas.pack(padx=0, pady=0)
        canvas.place(x=0, y=0)

        file_img1 = resource_path("KlasCroller\\img\\back.png")
        img1 = PhotoImage(file=file_img1)
        canvas.create_image(200, 250, image=img1)
        
        label_title = Label(master=self.win_notice_func3)
        label_title.config(text = "[SF MBTI]",font=font1,foreground='white', background='#7C1B0F',justify= CENTER)
        label_title.place(x=110,y=100)
        
        label_content = Label(master=self.win_notice_func3)
        label_content.config(text = " 지난 학기동안 당신은 어떻게\n\n학업을 수행하셨을까요?\n\n\n당신의 학업 성취 스타일과 맞는\n\n동물 사진을 출력해드립니다.",font=font,foreground='white', background='#7C1B0F',justify= CENTER)
        label_content.place(x=95,y=150)
        
        button_select_1 = Button(self.win_notice_func3, command= self.OpenWindow_PrintUserStyle)
        button_select_1.config(text="확인하기",bg='#7C1B0F',fg='snow',font=font)
        button_select_1.place(x=160,y=350,width=80,height=25)
        
        self.win_notice_func3.mainloop()
        
    def OpenWindow_PrintUserStyle(self):
        window_func_3 = Toplevel(self.win_notice_func3)
        window_func_3.config(bg='#7C1B0F')
        window_func_3.title('hi')
        window_func_3.geometry("650x400")
        window_func_3.resizable(width = FALSE, height = FALSE)
        
        Label(text="안녕하세요.....").place(1,1)
        
        
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
        