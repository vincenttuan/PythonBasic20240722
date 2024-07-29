# 隨機數的應用
# Lotto 電腦選號
import random  # 隨機套件

if __name__ == '__main__':
    print(random.random())  # 得到一個 0~1 之間的隨機數
    # 四星彩電腦選號
    n1 = random.randint(0, 9)  # 一個 0~9 的隨機數
    n2 = random.randint(0, 9)  # 一個 0~9 的隨機數
    n3 = random.randint(0, 9)  # 一個 0~9 的隨機數
    n4 = random.randint(0, 9)  # 一個 0~9 的隨機數
    print(n1, n2, n3, n4)
