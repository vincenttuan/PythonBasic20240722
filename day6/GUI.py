# 利用 thinker 來顯示 GUI
import tkinter

if __name__ == '__main__':
    win = tkinter.Tk()

    # 視窗上方標題
    win.title('IQ')

    # 視窗大小
    win.geometry("200x200")

    # 啟用視窗主程序
    win.mainloop()
