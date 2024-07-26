# if elif else 條件判斷應用
# 1.判斷是否及格
# 2.判斷級別是 A, B, C, D, F
score = input('請輸入成績:')  # input 會得到字串資料
score = int(score)  # 將字串轉整數, 注意 ! 一定要加
print("成績:", score, end=" ")

# 1.判斷是否及格
if score >= 60:
    print("及格")
else:
    print("不及格")

# 2.判斷級別是 A, B, C, D, F
# 90 <= score <= 100  "A"
# 80 <= score < 90    "B"
# 70 <= score < 80    "C"
# 60 <= score < 70    "D"
#  0 <= score < 60    "F" <- Fail
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("F")
else:
    print("成績錯誤")


