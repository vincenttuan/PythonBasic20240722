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


if __name__ == '__main__':
    # 建立飲料單
    menu = [
        Beverage('紅茶', 'S', 10),
        Beverage('紅茶', 'M', 15),
        Beverage('紅茶', 'L', 20),
        Beverage('紅茶冰', 'S', 15),
        Beverage('紅茶冰', 'M', 20),
        Beverage('紅茶冰', 'L', 25),
        Beverage('綠茶', 'S', 12),
        Beverage('綠茶', 'M', 18),
        Beverage('綠茶', 'L', 23),
        Beverage('奶茶', 'S', 20),
        Beverage('奶茶', 'M', 25),
        Beverage('奶茶', 'L', 30),
    ]
    for beverage in menu:
        print(beverage)






