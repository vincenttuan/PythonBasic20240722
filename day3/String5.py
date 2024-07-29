
def calc_bmi(index):
    h = float(heights[index])
    w = float(weights[index])
    bmi = w / (h / 100) ** 2
    print(h, w, bmi)


# 字串分組練習
# int("字串") 字串轉整數
# float("字串") 字串轉浮 點數
data1 = "170,160.5,180"  # 身高cm
data2 = "60,45,89.5"  # 體重kg
# 請計算出每組 bmi=?
heights = data1.split(",")
weights = data2.split(",")
print(heights, weights)
#--------------------------------
calc_bmi(0)
calc_bmi(1)
calc_bmi(2)

