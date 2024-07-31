# 利用 for 步進敘述, 產生 4 個 0~9 之間的隨機數
import random

if __name__ == '__main__':
    for i in range(0, 4):
        number = random.randint(0, 9)
        print(number, end=' ')

