import tkinter
from tkinter import font
'''
+------+-------------+
| btn1 |    btn2     |
+------+------+------+
| btn3 | btn3 | btn4 |
+-------------+------+
'''
win = tkinter.Tk()
# 設定字型,大小與風格
myfont = font.Font(family='Arial', size=50, weight='bold')
# 宣告按鈕
btn1 = tkinter.Button(text='Btn1', font=myfont)
btn2 = tkinter.Button(text='Btn2', font=myfont)
btn3 = tkinter.Button(text='Btn3', font=myfont)
btn4 = tkinter.Button(text='Btn4', font=myfont)
btn5 = tkinter.Button(text='Btn5', font=myfont)
btn6 = tkinter.Button(text='Btn6', font=myfont)
btn7 = tkinter.Button(text='Btn7', font=myfont)

btn1.grid(row=0, column=0, sticky='EWNS')   # EWNS: 無縫隙元件填滿
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=0, rowspan=2, sticky='EWNS')
btn4.grid(row=1, column=1, sticky='EWNS')
btn5.grid(row=1, column=2, sticky='EWNS')
btn6.grid(row=2, column=1, sticky='EWNS')
btn7.grid(row=2, column=2, sticky='EWNS')

win.mainloop()





