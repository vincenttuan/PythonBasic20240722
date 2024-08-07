import tkinter
from tkinter import font

'''
BMI 計算機
+--------+---------+
| Height |  170.0  |  <-- Label, Entry
+--------+---------+
| Weight |   60.5  |  <-- Label, Entry
+--------+---------+
|  Reset |  Submit |  <-- Button, Button
+--------+---------+
|      20.76       |  <-- Label, Label
+--------+---------+
'''

def submit():  # 計算 bmi
    pass

def reset():  # 重製
    pass

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('BMI 計算機')
    win.geometry("600x250")
    # 建立 GUI 元件
    myfont = font.Font(family='Arial', size=30, weight='bold')
    height_label = tkinter.Label(text='身高', font=myfont)
    height_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
    weight_label = tkinter.Label(text='體重', font=myfont)
    weight_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
    reset_btn = tkinter.Button(text='清除', font=myfont, command=reset)
    submit_btn = tkinter.Button(text='計算', font=myfont, command=submit)
    result_label = tkinter.Label(text='0.00', font=myfont)
    # ------------------------------------------------------------------
    # 布局 GUI 元件
    height_label.grid(row=0, column=0, sticky='EWNS')
    height_entry.grid(row=0, column=1, sticky='EWNS')
    weight_label.grid(row=1, column=0, sticky='EWNS')
    weight_entry.grid(row=1, column=1, sticky='EWNS')
    reset_btn.grid(row=2, column=0, sticky='EWNS')
    submit_btn.grid(row=2, column=1, sticky='EWNS')
    result_label.grid(row=3, column=0, columnspan=2, sticky='EWNS')
    # ------------------------------------------------------------------
    win.mainloop()








