# 利用 for 模擬搭電梯
import time

min = int(input('請輸入最低樓層:'))  # 最低樓層
max = int(input('請輸入最高樓層:'))  # 最高樓層
print('本大樓有%d~%d層' % (min, max))
target_floor = int(input('請輸入樓層:'))
# 防呆
if min <= target_floor <= max:
    for floor in range(min, max + 1):
        print('電梯上樓', floor)
        time.sleep(1)  # 停一秒
        if floor == target_floor:
            print('電梯到達指定樓層, 請出電梯')
            break  # for 迴圈結束
else:
    print('樓層輸入不正確')

print("程式結束!")


