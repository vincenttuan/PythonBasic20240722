import matplotlib.pyplot as plt
# 學生成績列表 + 繪製折線圖
students = {'John': 90, 'Mary': 85, 'Jack': 100, 'Rose': 45, 'Helen': 72}

if __name__ == '__main__':
    print(students)
    # 分離觀察學生名稱與分數
    names = list(students.keys())
    scores = list(students.values())
    print(names)
    print(scores)

    # 繪製折線圖
    plt.plot(names, scores)
    # 顯示圖型
    plt.show()


