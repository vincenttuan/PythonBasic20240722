# 物件導向
# 飲料店
# 飲料類別 Beverage
# 飲料名 name, 大小 size, 價格 price
# 紅茶 S 10, 紅茶 M 15, 紅茶 L 20
# 紅茶冰 S 15, 紅茶冰 M 20, 紅茶冰 L 25
# 綠茶 S 12, 綠茶 M 18, 綠茶 L 23
# 奶茶 S 20, 奶茶 M 25, 奶茶 L 30
# -------------------------------------
class Beverage:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self) -> str:
        return "%s %s $%d" % (self.name, self.size, self.price)


def get_menu():
    return [
        Beverage('紅茶', 'S', 10),  # 0
        Beverage('紅茶', 'M', 15),  # 1
        Beverage('紅茶', 'L', 20),  # 2
        Beverage('紅茶冰', 'S', 15),  # 3
        Beverage('紅茶冰', 'M', 20),  # 4
        Beverage('紅茶冰', 'L', 25),  # 5
        Beverage('綠茶', 'S', 12),  # 6
        Beverage('綠茶', 'M', 18),  # 7
        Beverage('綠茶', 'L', 23),  # 8
        Beverage('奶茶', 'S', 20),  # 9
        Beverage('奶茶', 'M', 25),  # 10
        Beverage('奶茶', 'L', 30),  # 11
    ]


if __name__ == '__main__':
    # 建立飲料單
    menu = get_menu()

    print("Menu:")
    print("----------------")
    for beverage in menu:
        print(beverage)

    # 訂單
    order = [menu[0], menu[4], menu[4], menu[4], menu[8], menu[10]]
    print("\nOrder:")
    print("----------------")
    for beverage in order:
        print(beverage)
    # 計算此筆訂單總金額
    total_sum = sum(beverage.price for beverage in order)
    print("訂單總金額: %d" % total_sum)





