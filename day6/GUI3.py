import tkinter
# 利用 thinker 來顯示 GUI
'''
    +------------+
    |     5      |
    | Add   Exit |
    +------------+
按下 Add 上方數字會自動 + 1
按下 Exit 會離開視窗
'''
# 自動 + 1
def add():
    pass

# 離開視窗
def win_exit():
    pass

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title("Add Play")
    win.geometry("300x300")
    # 設定變數
    number = tkinter.StringVar()  # 字串參照物件(tkinter專用)
    number.set("0")  # 給定預設值
    # label 配置
    label = tkinter.Label(win, textvariable=number, bg='green', fg='yellow',
                          font=('Arial', 30), width=30, height=5)
    label.pack()
    # button 配置
    # command 表示按下 button 後要執行的函式
    add_button = tkinter.Button(win, text="Add", font=('Arial', 20), width=10, height=2, command=add)
    exit_button = tkinter.Button(win, text="exit", font=('Arial', 20), width=10, height=2, command=win_exit)
    add_button.pack(side=tkinter.LEFT)
    exit_button.pack(side=tkinter.RIGHT)

    # 視窗運行
    win.mainloop()






