# Exception 例外處理
# ZeroDivisionError: 除以0的錯誤
# IndexError: index 超過陣列最大範圍
a = 10
b = [2, 0]
try:
    #print(a/b[0])  # 等於 10/2
    #print(a/b[1])  # 等於 10/0
    print(a/b[2])  # 等於 10/?
except ZeroDivisionError as e:
    print("找到數學錯誤:", e, e.__class__)
except IndexError as e:
    print("找到索引錯誤:", e, e.__class__)
except Exception as e:
    print("找到其他錯誤:", e, e.__class__)
else:
    print("OK")



