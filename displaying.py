from tkinter import *
import os
import sys

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
    def __init__(self):
        self.id = 0;
        self.pw = '';
        
        # window
        self.win = [_ for _ in range(5)]
        # label
        self.label = [_ for _ in range(10)]
        # button
        self.button = [_ for _ in range(10)]
        # entry
        self.entry = [_ for _ in range(10)]
        # image
        self.img = [_ for _ in range(5)]
    
    def __del__(self):
        print()
        
    # 로그인 용 Window 설정
    def SetWindow_Login(self):
        self.win[0] = Tk()
        self.button[0] = Button(self.win[0])
        for i in range(4):
            self.label[i] = Label(self.win[0])
        for i in range(2):
            self.entry[i] = Entry(self.win[0])
        # 창 설정
        self.win[0].title("Klas Log-in")
        self.win[0].geometry("425x650")
        self.win[0].option_add("*Font", "맑은고딕 25")
        # id 라벨
        self.label[1] = Label(self.win[0])
        self.label[1].config(text = "ID")
        # id 입력
        self.entry[0] = Entry(self.win[0], relief = "groove")
        self.entry[0].insert(0,"학번을 입력하세요.")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.entry[0].get() == "학번을 입력하세요.":
                self.entry[0].delete(0, len(self.entry[0].get()))
        self.entry[0].bind("<Button-1>",clear)
        # pw 라벨
        self.label[2] = Label(self.win[0])
        self.label[2].config(text = "Password")
        # pw 입력
        self.entry[1] = Entry(self.win[0])
        self.entry[1].config(show="*")
        # 광운대학교 로고
        self.img[0] = PhotoImage(file = resource_path("KlasCroller\\img\\kwang.png"),master = self.win[0])
        self.img[0] = self.img[0].subsample(1)
        self.label[0].config(image = self.img[0])
        # 로그인 버튼 설정
        self.button[0].config(text="로그인",width=5,command=self.EventHandler_Login)

    # 로그인 용 Window 열기
    def OpenWindow_Login(self):
        self.SetWindow_Login()
        self.label[0].grid(row=1, column=2)
        self.label[1].grid(row=3, column=2)
        self.entry[0].grid(row=4, column=2)
        self.label[2].grid(row=5, column=2)
        self.entry[1].grid(row=6, column=2)
        self.button[0].grid(row=7, column=2)
        self.label[3].grid(row=7, column=2)
        self.win[0].mainloop()

    def GetIdPw(self):
        self.OpenWindow_Login()
        return self.id,self.pw

    # 로그인 이벤트 핸들러
    def EventHandler_Login(self):
        self.id = self.entry[0].get()
        self.pw = self.entry[1].get()
        self.win[0].destroy()
        
    # 두번째 기능선택 창 구현
    def SetWindow_MainMenu(self):
        self.win_func = Tk()
        self.win_func.title("Klas function")
        self.win_func.geometry("650x400") # 가로 세로
        self.win_func.option_add("*Font", "맑은고딕 25")
        self.label1 = Label(self.win_func, text = '기능 선택')
        
        # 기능 선택 버튼
        self.b1 = Button(self.win_func, text = "완료 학기\n 분석", command = self.FuncEventHandler1)
        self.b2 = Button(self.win_func, text = "학기 간 \n비교 분석", command = self.FuncEventHandler2)
        self.b3 = Button(self.win_func, text = "학점 mbit", command = self.FuncEventHandler3)

    # 첫번째 기능 선택 이벤트 핸들러(현재 학기 분석하기)
    def FuncEventHandler1(self):
        
        self.win_sem1 = Tk()
        self.win_sem1.title("Klas semester1")
        self.win_sem1.geometry("400x300")
        self.win_sem1.option_add("*Font", "맑은고딕 25")
        self.label1 = Label(self.win_sem1, text = "현재 학기 분석하기")
        self.label1.pack()

        # 학기 선택 버튼
        for i in range(len(self.sem_list)-1):
            if i == 0:
                self.b0 = Button(self.win_sem1, text = self.sem_list[0], command = self.DataEventHandler1)
                self.b0.pack()
            elif i == 1:
                self.b1 = Button(self.win_sem1, text = self.sem_list[1], command = self.DataEventHandler2)
                self.b1.pack()
            elif i == 2:
                self.b2 = Button(self.win_sem1, text = self.sem_list[2], command = self.DataEventHandler3)
                self.b2.pack()
            elif i == 3:
                self.b3 = Button(self.win_sem1, text = self.sem_list[3], command = self.DataEventHandler4)
                self.b3.pack()
            elif i == 4:
                self.b4 = Button(self.win_sem1, text = self.sem_list[4], command = self.DataEventHandler5)
                self.b4.pack()
            elif i == 5:
                self.b5 = Button(self.win_sem1, text = self.sem_list[5], command = self.DataEventHandler6)
                self.b5.pack()
            elif i == 6:
                self.b6 = Button(self.win_sem1, text = self.sem_list[6], command = self.DataEventHandler7)
                self.b6.pack()
            elif i == 7:
                self.b7 = Button(self.win_sem1, text = self.sem_list[7], command = self.DataEventHandler8)
                self.b7.pack()
            elif i == 8:
                self.b8 = Button(self.win_sem1, text = self.sem_list[8], command = self.DataEventHandler9)
                self.b8.pack()
            elif i == 9:
                self.b9 = Button(self.win_sem1, text = self.sem_list[9], command = self.DataEventHandler10)
                self.b9.pack()
        
        self.win_sem1.mainloop()


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
        
    # 기능선택 창에서 첫번째 학기 선택 이벤트 핸들러
    def DataEventHandler1(self):
        self.win_data1 = Tk()
        self.win_data1.title("Klas data1")
        self.win_data1.geometry("400x300")
        self.win_data1.option_add("*Font", "맑은고딕 25")
        self.label1 = Label(self.win_data1, text = self.sem_list[0] + "학기 분석하기")
        self.label1.pack()

    # 기능선택 창에서 두번째 학기 선택 이벤트 핸들러
    def DataEventHandler2(self):
        self.win_data2 = Tk()
        self.win_data2.title("Klas data2")
        self.win_data2.geometry("400x300")
        self.win_data2.option_add("*Font", "맑은고딕 25")
        self.label2 = Label(self.win_data2, text = self.sem_list[1] + "학기 분석하기")
        self.label2.pack()

    # 기능선택 창에서 세번째 학기 선택 이벤트 핸들러
    def DataEventHandler3(self):
        self.win_data3 = Tk()
        self.win_data3.title("Klas data3")
        self.win_data3.geometry("400x300")
        self.win_data3.option_add("*Font", "맑은고딕 25")
        self.label3 = Label(self.win_data3, text = self.sem_list[2] + "학기 분석하기")
        self.label3.pack()

    # 기능선택 창에서 네번째 학기 선택 이벤트 핸들러
    def DataEventHandler4(self):
        self.win_data4 = Tk()
        self.win_data4.title("Klas data4")
        self.win_data4.geometry("400x300")
        self.win_data4.option_add("*Font", "맑은고딕 25")
        self.label4 = Label(self.win_data4, text = self.sem_list[3] + "학기 분석하기")
        self.label4.pack()

    # 기능선택 창에서 다번째 학기 선택 이벤트 핸들러
    def DataEventHandler5(self):
        self.win_data5 = Tk()
        self.win_data5.title("Klas data5")
        self.win_data5.geometry("400x300")
        self.win_data5.option_add("*Font", "맑은고딕 25")
        self.label5 = Label(self.win_data5, text = self.sem_list[4] + "학기 분석하기")
        self.label5.pack()

    # 기능선택 창에서 여섯번째 학기 선택 이벤트 핸들러
    def DataEventHandler6(self):
        self.win_data6 = Tk()
        self.win_data6.title("Klas data6")
        self.win_data6.geometry("400x300")
        self.win_data6.option_add("*Font", "맑은고딕 25")
        self.label6 = Label(self.win_data6, text = self.sem_list[5] + "학기 분석하기")
        self.label6.pack()

    # 기능선택 창에서 일곱번째 학기 선택 이벤트 핸들러
    def DataEventHandler7(self):
        self.win_data7 = Tk()
        self.win_data7.title("Klas data7")
        self.win_data7.geometry("400x300")
        self.win_data7.option_add("*Font", "맑은고딕 25")
        self.label7 = Label(self.win_data7, text = self.sem_list[6] + "학기 분석하기")
        self.label7.pack()

    # 기능선택 창에서 여덟번째 학기 선택 이벤트 핸들러
    def DataEventHandler8(self):
        self.win_data8 = Tk()
        self.win_data8.title("Klas data8")
        self.win_data8.geometry("400x300")
        self.win_data8.option_add("*Font", "맑은고딕 25")
        self.label8 = Label(self.win_data8, text = self.sem_list[7] + "학기 분석하기")
        self.label8.pack()

    # 기능선택 창에서 아홉번째 학기 선택 이벤트 핸들러
    def DataEventHandler9(self):
        self.win_data9 = Tk()
        self.win_data9.title("Klas data9")
        self.win_data9.geometry("400x300")
        self.win_data9.option_add("*Font", "맑은고딕 25")
        self.label9 = Label(self.win_data9, text = self.sem_list[8] + "학기 분석하기")
        self.label9.pack()

    # 기능선택 창에서 열번째 학기 선택 이벤트 핸들러
    def DataEventHandler10(self):
        self.win_data10 = Tk()
        self.win_data10.title("Klas data10")
        self.win_data10.geometry("400x300")
        self.win_data10.option_add("*Font", "맑은고딕 25")
        self.label10 = Label(self.win_data10, text = self.sem_list[9] + "학기 분석하기")
        self.label10.pack()

