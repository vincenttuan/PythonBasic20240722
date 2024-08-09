# 物件導向
class Student:   # 類別, 建構物件的藍圖
    name = None    # 姓名, 物件屬性/變數/欄位/資產
    age = 0      # 年齡, 物件屬性/變數/欄位/資產
    gender = None  # 性別, 物件屬性/變數/欄位/資產

    def __str__(self) -> str:
        return "姓名:%s 年齡:%d 性別:%s" % (self.name, self.age, self.gender)


if __name__ == '__main__':
    s1 = Student()
    s1.name = 'John'
    s1.age = 16
    s1.gender = '男'
    print(s1)

