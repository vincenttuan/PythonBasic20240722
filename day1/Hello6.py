# 變數的應用 2
# 計算 bmi
w = 60  # 體重(kg)
h = 170  # 身高(cm)
print("體重kg:", w, "身高cm", h)  # 印出變數內容

h = h / 100  # 身高(cm)轉身高(m)
print("體重kg:", w, "身高m", h)  # 印出變數內容

bmi = w / (h**2)
print("BMI:", bmi)

# 若只要印出到小數點 2 位  ?
# 利用 %f 進行浮點數格式化
print("BMI: %.2f" % bmi)
