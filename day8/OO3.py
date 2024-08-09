# 物件導向
class Student:   # 類別, 建構物件的藍圖
    name = None    # 姓名, 物件屬性/變數/欄位/資產
    age = 0      # 年齡, 物件屬性/變數/欄位/資產
    gender = None  # 性別, 物件屬性/變數/欄位/資產

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return "姓名:%s 年齡:%d 性別:%s" % (self.name, self.age, self.gender)


if __name__ == '__main__':
    s1 = Student('John', 16, '男')
    s2 = Student('Mary', 15, '女')
    s3 = Student('Steven', 10, '男')
    print(s1, s2, s3)
    students = [s1, s2, s3]
    # 年齡總和
    total_age = sum(student.age for student in students)
    # 年齡平均
    average_age = total_age / len(students)
    print("平均年齡: %.1f 歲" % average_age)



