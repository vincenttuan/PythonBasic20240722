# 利用 for 模擬搭電梯
import time

print('本大樓有1~7層')
target_floor = int(input('請輸入樓層:'))
# 防呆
if 1 <= target_floor <= 7:
    for floor in range(1, 8):
        print('電梯上樓', floor)
        time.sleep(1)  # 停一秒
        if floor == target_floor:
            print('電梯到達指定樓層, 請出電梯')
            break  # for 迴圈結束
else:
    print('樓層輸入不正確')

print("程式結束!")


