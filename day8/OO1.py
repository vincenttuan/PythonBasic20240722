# 物件導向
class Student:   # 類別, 建構物件的藍圖
    name = None    # 姓名, 物件屬性/變數/欄位/資產
    age = 0      # 年齡, 物件屬性/變數/欄位/資產
    gender = None  # 性別, 物件屬性/變數/欄位/資產


# 主程式
if __name__ == '__main__':
    p1 = Student()  # 建立學生物件
    p2 = Student()  # 建立學生物件
    # -- 設定物件資料 -------------------
    p1.name = 'John'; p1.age = 16; p1.gender = '男'
    p2.name = 'Mary'
    p2.age = 15
    p2.gender = '女'
    # ----------------------------------
    print(p1.name, p1.age, p1.gender)
    print(p2.name, p2.age, p2.gender)
