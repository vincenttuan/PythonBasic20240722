# 數學套件應用 - 二點間的距離
import math

x1, y1 = 10, 20  # A點座標
x2, y2 = 30, 40  # B點座標
print("A點座標:(%d, %d)" % (x1, y1))
print("B點座標:(%d, %d)" % (x2, y2))

dx = (x1 - x2)**2
# 也可以寫成 dx = math.pow(x1 - x2, 2)
dy = (y1 - y2)**2

d = math.sqrt(dx + dy)
print("距離: %.2f" % d)





