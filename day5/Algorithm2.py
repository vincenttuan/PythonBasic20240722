# 演算法
# 買 x 送 y 透過自訂函式
def calculate_total_price(price, amount, x, y):
    # 根據 x, y 先算出要付幾瓶的錢
    bottles = amount // (x + y) * x + amount % (x + y)
    # 計算付款金額
    total = bottles * price
    return total  # 將金額計算完後回傳


# 主程式
if __name__ == '__main__':
    # 飲料 10 元, 買進 9 瓶, 買 5 送 2 要花多少錢 ?
    total = calculate_total_price(10, 9, 5, 2)
    print("飲料 10 元, 買進 9 瓶, 買 5 送 2 要花多少錢: %d 元" % total)
    # 飲料 15 元, 買進 18 瓶, 買 10 送 3 要花多少錢 ?
    total = calculate_total_price(15, 18, 10, 3)
    print("飲料 15 元, 買進 18 瓶, 買 10 送 3 要花多少錢: %d 元" % total)
