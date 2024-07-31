# 利用 for 求質數
# 使用者輸入一個數字來判定是否是質數

if __name__ == '__main__':
    n = int(input('請輸入一個數字:'))
    is_prime = True  # 預設是質數
    # 判斷是否是質數 -------------------------
    for i in range(2, n):
        if n % i == 0:  # 若 n 整除 i (n 除以 i 的餘數等於 0)
            is_prime = False
            break  # 跳離迴圈
    # --------------------------------------
    if is_prime:  # 相當於 is_prime == True
        print("%d 是質數" % n)
    else:
        print("%d 不是質數" % n)
