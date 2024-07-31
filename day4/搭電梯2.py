# 模擬連續搭電梯, 輸入 0 退出程式
import time

if __name__ == '__main__':
    min = 1  # 最低樓層
    max = 10  # 最高樓層
    print('本大樓有 %d~%d 層' % (min, max))
    current_floor = min  # 目前電梯所在位置
    while True:
        target_floor = int(input('請輸入目標樓層:'))
        if min <= target_floor <= max:
            # 電梯運作邏輯
            if target_floor > current_floor:
                direction = '上樓'
            elif target_floor < current_floor:
                direction = '下樓'
            else:  # 目標樓層就是目前電梯所在地
                continue  # 重跑 while 回圈

            while current_floor != target_floor:
                print('電梯 %s 目前在 %d 樓' % (direction, current_floor))
                time.sleep(1)
                if direction == '上樓':
                    current_floor = current_floor + 1  # 每次 +1
                else:
                    current_floor = current_floor - 1  # 每次 -1

            print('電梯已到 %d 樓' % current_floor)

        else:
            print('樓層不存在請重新輸入')
            continue  # 重跑 while 回圈



