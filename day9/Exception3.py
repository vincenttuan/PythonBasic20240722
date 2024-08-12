# Exception 例外處理應用
# 使用者輸入半徑之後系統可以計算出圓面積
import math


def user_input():
    while True:
        r = input('請輸入半徑:')
        try:
            r = float(r)  # 字串轉浮點數
        except ValueError as e:
            print('輸入錯誤請重新輸入')
            continue  # 重跑回圈
        else:
            area = r ** 2 * math.pi
            print("半徑: %.1f 圓面積: %.1f" % (r, area))
            break  # 跳出迴圈


if __name__ == '__main__':
    user_input()
