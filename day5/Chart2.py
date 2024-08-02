import matplotlib.pyplot as plt
# 二次段考成績列表 + 繪製折線圖
students1 = {'John': 90, 'Mary': 85, 'Jack': 100, 'Rose': 45, 'Helen': 72}
students2 = {'John': 85, 'Mary': 77, 'Jack': 35, 'Rose': 80, 'Helen': 99}

if __name__ == '__main__':
    # 分離觀察學生名稱與分數:第一次段考
    names1 = list(students1.keys())
    scores1 = list(students1.values())
    # 分離觀察學生名稱與分數:第二次段考
    names2 = list(students2.keys())
    scores2 = list(students2.values())

    # 繪製折線圖
    plt.plot(names1, scores1, 'o-', color='red', label="Exam 1")
    plt.plot(names2, scores2, '*-', color='blue', label="Exam 2")

    # 設定圖標資訊
    plt.xlabel('student name')
    plt.ylabel('score')
    plt.title('Comparison of Student Scores')

    # 顯示圖型
    plt.show()

