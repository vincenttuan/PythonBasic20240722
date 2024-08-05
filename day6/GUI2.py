# 利用 thinker 來顯示 GUI
'''
    +--------+
    |  Label |
    | B1  B2 |
    +--------+
'''
import tkinter

if __name__ == '__main__':
    win = tkinter.Tk()

    hello_label = tkinter.Label(win,
                                text="Hello",  # 標籤文字
                                bg='green',    # 背景顏色
                                fg='yellow',   # 前景顏色(字體顏色)
                                font=('Arial', 20),  # 字型與大小
                                width=15,  # 標籤寬度
                                height=2   # 標籤高度
                                )
    hello_label.pack()  # 將 hello_label 配置在 win 中

    b1 = tkinter.Button(win, text="Prev")
    b1.pack(side=tkinter.LEFT)  # 配置在左

    b2 = tkinter.Button(win, text="Next")
    b2.pack(side=tkinter.RIGHT)  # 配置在右

    win.mainloop()




