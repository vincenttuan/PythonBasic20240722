# 四星彩電腦選號
import random  # 匯入亂數/隨機數套件

a, b = 0, 9  # 設定 a, b 二個變數預設內容放 0, 9

x1 = random.randint(a, b)
x2 = random.randint(a, b)
x3 = random.randint(a, b)
x4 = random.randint(a, b)

print("四星彩電腦選號:", x1, x2, x3, x4)


