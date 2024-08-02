# 演算法
# 買 x 送 y
if __name__ == '__main__':
    price = 10  # 飲料價格
    amount = 5  # 購買數量
    x, y = 2, 1  # 買 x 送 y
    print("飲料 %d 元 買 %d 送 %d 買進 %d 瓶須支付多少錢?" % (price, x, y, amount))
    # 試問應付多少錢 ?
    # 根據 x, y 先算出要付幾瓶的錢
    bottles = amount // (x+y) * x + amount % (x+y)
    print("需支付 %d 瓶的錢" % bottles)
    # 計算付款金額
    total = bottles * price
    print("付款金額 %d" % total)


