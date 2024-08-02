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
    #plt.plot(names, scores, '*--', color='red')
    # 繪製長條圖
    #plt.bar(names, scores, color='blue')
    # 繪製圓餅圖
    plt.pie(scores, labels=names, autopct='%.1f%%', startangle=140)

    # 設定圖標資訊
    plt.xlabel('student name')
    plt.ylabel('score')
    plt.title('student score chart')
    # 顯示圖型
    plt.show()


