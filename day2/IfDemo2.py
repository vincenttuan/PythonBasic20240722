# if else 簡單表達式
score = 75
print(score)
# 一般表達式 --------------------
if score >= 60:
    print("及格")
else:
    print("不及格")
# 簡單表達式 ----------------------
print("及格" if score >= 60 else "不及格")
# 簡單表達式 ----------------------
result = "及格" if score >= 60 else "不及格"  # 將判斷結果放到 result 變數中
print(result)  # 印出 result 變數內容

