# 字串分組練習
# int("字串") 字串轉整數
# float("字串") 字串轉浮 點數
data1 = "170,160.5,180"  # 身高cm
data2 = "60,45,89.5"  # 體重kg
# 請計算出每組 bmi=?
heights = data1.split(",")
weights = data2.split(",")
print(heights, weights)
# ----------------------------
h1 = float(heights[0])
w1 = float(weights[0])
bmi1 = w1 / (h1/100)**2
print(h1, w1, bmi1)
# ----------------------------
h2 = float(heights[1])
w2 = float(weights[1])
bmi2 = w2 / (h2/100) ** 2
print(h2, w2, bmi2)
# ----------------------------
h3 = float(heights[2])
w3 = float(weights[2])
bmi3 = w3 / (h3/100) ** 2
print(h3, w3, bmi3)




