# 整合應用-找零錢程式
# 買飲料一瓶 23 元, 付了 100 元, 請問要找幾元 ?
# 如何找 ? 50元 1 個, 10元 2 個, 5元 1 個, 1元 個
price = 23  # 價格 23 元
pay = 100  # 付款金額 100 元
exchange = pay - price  # 找錢 77 元
print("飲料:", price, "付款:", pay, "應找:", exchange)
fifty = exchange // 50
print("50元 %d 個" % fifty)
exchange = exchange - fifty * 50  # 剩下 27 元
ten = exchange // 10
print("10元 %d 個" % ten)
exchange = exchange - ten * 10  # 剩下 7 元
five = exchange // 5
print("5元 %d 個" % five)
one = exchange - five * 5  # 剩下 2 元
print("1元 %d 個" % one)
