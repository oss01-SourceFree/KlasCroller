from tkinter import *

class WindowManager():
    def __init__(self):
        self.id = 0;
        self.pw = '';
        self.win = Tk()
        
        # label
        self.label = [_ for _ in range(10)]
        # button
        self.button = [_ for _ in range(10)]
        # entry
        self.entry = [_ for _ in range(10)]
    
    def __del__(self):
        print()
        
    # 로그인 용 Window 설정
    def SetWindowForLogin(self):
        self.button[0] = Button(self.win)
        for i in range(4):
            self.label[i] = Label(self.win)
        for i in range(2):
            self.entry[i] = Entry(self.win)
                
        # 창 설정
        self.win.title("Klas Log-in")
        self.win.geometry("400x300")
        self.win.option_add("*Font", "맑은고딕 25")
        
        # id 라벨
        self.label[1] = Label(self.win)
        self.label[1].config(text = "ID")
        #lab1.configure(bg='black')
        
        # id 입력
        self.entry[0] = Entry(self.win, relief = "groove")
        self.entry[0].insert(0,"학번을 입력하세요.")
        def clear(event):
            # 좌클릭 했을 때 입력창의 내용 다 지우기
            if self.entry[0].get() == "학번을 입력하세요.":
                self.entry[0].delete(0, len(self.entry[0].get()))
        self.entry[0].bind("<Button-1>",clear)
        
        # pw 라벨
        self.label[2] = Label(self.win)
        self.label[2].config(text = "Password")
        
        # pw 입력
        self.entry[1] = Entry(self.win)
        self.entry[1].config(show="*")
        
        # 메시지 라벨
        self.label[3] = Label(self.win)
        
        # 로그인 버튼 설정
        self.button[0].config(text="로그인",width=5,command=self.LoginEventHandler)

    # 로그인 용 Window 열기
    def OpenWindowForLogin(self):
        self.SetWindowForLogin()
        self.label[1].pack()
        self.entry[0].pack()
        self.label[2].pack()
        self.entry[1].pack()
        self.button[0].pack()
        self.label[3].pack()
        self.win.mainloop()
    
    # 로그인 이벤트 핸들러
    def LoginEventHandler(self):
        
        self.id = self.entry[0].get()
        self.pw = self.entry[1].get()
        self.win.destroy()
        
    def GetIdPw(self):
        self.OpenWindowForLogin()
        return self.id,self.pw














# def getIdPw():
#     openWindowForLogin()
#     return klas_id,klas_pw

# def openWindowForLogin():
#     # lab_k.pack()
#     lab1.pack()
#     ent1.pack()
#     lab2.pack()
#     ent2.pack()
#     btn.pack()
#     # 메시지 라벨
#     lab3 = Label(win)
#     lab3.pack()
#     win.mainloop()


# # 로그인 이벤트 핸들러
# def closeWindowForLogin():
#     global klas_id,klas_pw
#     klas_id = ent1.get()
#     klas_pw = ent2.get()
#     win.destroy()

# win = Tk()
# win.title("Klas Log-in")
# win.geometry("400x300")
# win.option_add("*Font", "맑은고딕 25")

# # # 광운 로고
# # lab_k = Label(win)
# # img = PhotoImage(file = "kwang.png", master = win)
# # img = img.subsample(1)
# # lab_k.config(image = img)

# # id 라벨
# lab1 = Label(win)
# lab1.config(text = "ID")
# lab1.configure(bg='black')

# # id 입력창
# ent1 = Entry(win, relief="groove")
# ent1.insert(0, "학번을 입력하세요")
# def clear(event):
#     # 좌클릭 했을 때 입력창의 내용 다 지우기
#     if ent1.get() == "학번을 입력하세요":
#         ent1.delete(0, len(ent1.get()))
# ent1.bind("<Button-1>", clear)

# # pw 라벨
# lab2 = Label(win)
# lab2.config(text = "Password")

# # pw 입력창
# ent2 = Entry(win)
# ent2.config(show="*")

# # 로그인 버튼
# btn = Button(win)
# btn.config(text = "로그인", command=closeWindowForLogin)
# btn.config(width=5)

# # 메시지 라벨
# lab3 = Label(win)