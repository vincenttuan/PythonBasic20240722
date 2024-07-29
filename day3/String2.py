# 字串分析-進階版
words = "she sell sea shell on the sea shore"
# words 有幾個單字 ?
result = words.split(" ")  # 利用 split 來切割字串, result 存放切割後的結果
print(result)  # result 在這邊就是一個list(列表/陣列)
print(type(result))
print("單字數量:", len(result))
print("第一個單字:", result[0])
print("第二個單字:", result[1])
print("最後一個單字:", result[7])
print("最後一個單字:", result[len(result) - 1])



