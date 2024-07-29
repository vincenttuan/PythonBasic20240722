# 猜數字
import random

if __name__ == '__main__':
    ans = random.randint(1, 9)  # 產生一個答案
    while True:
        user_guess = int(input('使用者請輸入數字(1~9):'))
        if user_guess < ans:
            print('使用者猜小了')
        elif user_guess > ans:
            print('使用者猜大了')
        else:
            print('使用者猜中了, 好棒棒~')
            break  # 強制離開迴圈

    print("Game Over!")
