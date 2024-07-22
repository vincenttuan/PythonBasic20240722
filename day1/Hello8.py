# 整合應用-找零錢程式
# 買飲料一瓶 123 元, 付了 1000 元, 請問要找幾元 ? 如何找 ?
price = int(input('請輸入飲料價格:'))
pay = int(input('請輸入付款金額:'))
exchange = pay - price  # 找錢
print("飲料:", price, "付款:", pay, "應找:", exchange)
# 計算找零的面額與數量
# --------------------------------------------------
base = 500  # 面額
five_hundred = exchange // base
exchange = exchange - five_hundred * base
print("%d元 %d 個" % (base, five_hundred))
# --------------------------------------------------
base = 100  # 面額
one_hundred = exchange // base
exchange = exchange - one_hundred * base
print("%d元 %d 個" % (base, one_hundred))
# --------------------------------------------------
base = 50  # 面額
fifty = exchange // base
exchange = exchange - fifty * base
print("%d元 %d 個" % (base, fifty))
# --------------------------------------------------
base = 10  # 面額
ten = exchange // base
exchange = exchange - ten * base
print("%d元 %d 個" % (base, ten))
# --------------------------------------------------
base = 5  # 面額
five = exchange // base
exchange = exchange - five * base
print("%d元 %d 個" % (base, five))
# --------------------------------------------------
base = 1
one = exchange
print("%d元 %d 個" % (base, one))
# --------------------------------------------------
