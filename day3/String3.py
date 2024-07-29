data = "100,90,83,70,60"
print(data)
# 計算總分
scores = data.split(",")
print(scores)
total = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
print('總分:', total)
total = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3]) + int(scores[4])
print('總分:', total)
# 計算平均
average = total / len(scores)
print('平均:', average)
print("分數組數:", len(scores))

