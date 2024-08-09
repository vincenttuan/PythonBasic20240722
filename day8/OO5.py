# 飲料訂單系統
from day8.OO4 import get_menu

if __name__ == '__main__':
    menu = get_menu()
    print('Menu:')
    for index, beverage in enumerate(menu):
        print(index, beverage)
    # -------------------------------------
    print("-----------------")
    # 訂單
    order = []
    while True:
        data = input('請選擇商品代號(0~11), 離開請輸入(q) ==> ')
        if data == 'q':
            break
        index = int(data)  # 將 data 轉 int, 得到使用者所購買的商品代號
        # 判斷 index 範圍
        if index < 0 or index >= len(menu):
            print('飲料號碼超過範圍')
            break
        # 列印所購買的飲料
        print(menu[index])
        # 加入訂單
        order.append(menu[index])
    # -------------------------------------------------------
    print("\n訂單:")
    for beverage in order:
        print(beverage)
    # 計算此筆訂單總金額
    total_sum = sum(beverage.price for beverage in order)
    print("訂單總金額: %d" % total_sum)
