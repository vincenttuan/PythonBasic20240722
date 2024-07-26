# if else 簡單表達式
score = 90
print(score)
# 一般表達式 --------------------
if score >= 80:
    print("優等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 簡單表達式 --------------------
result = "優等" if score >= 80 else "及格" if score >= 60 else "不及格"
print(result)
