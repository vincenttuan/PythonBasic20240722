# 隨堂練習
# 1.印出 2~100 所有的質數
# 2.質數有幾個
# 3.並請計算所有質數的總和

if __name__ == '__main__':
    count = 0  # 紀錄質數有幾個
    total = 0  # 紀錄質數的總和
    for n in range(2, 101):
        is_prime = True
        # ----------------------
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        # ----------------------
        if is_prime:
            print(n, end=" ")
            count += 1
            total += n

    print('\n質數個數:', count)
    print('質數總和:', total)

