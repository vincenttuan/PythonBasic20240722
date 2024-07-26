import math
# 自訂函式
# 建立能夠計算圓面積與球體積的函式


def calculate_circle_area(radius):
    # 計算圓面積
    result = math.pi * radius ** 2
    print("半徑:%.1f 圓面積:%.2f" % (radius, result))


def calculate_sphere_volume(radius):
    # 計算球體積
    result = (4/3) * math.pi * radius ** 3
    print("半徑:%.1f 球體積:%.2f" % (radius, result))


r = 10.5
calculate_circle_area(r)
calculate_sphere_volume(r)

