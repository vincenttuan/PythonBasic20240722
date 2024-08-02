# 數組
# []     -> List 列表陣列, 元素內容可以重複
# set()  -> Set 列表陣列, 元素內容不 可以重複
# dict() -> 字典列表(key/value), key 不可重複, value 可以重複

a = [100, 50, 70, 30, 50]
#    0    1   2   3   4   <-- 位置(維度)
print(a)
# 變更元素位置=1的內容
a[1] = 95
print(a)
# 增加元素
a.append(60)
print(a)
# 移除指定元素內容
a.remove(30)  # 移除內容為 30 的元素
print(a)
# 移除指定位置的元素
a.__delitem__(2)  # 移除指定位置=2的元素
print(a)
#---------------------------------------
# 排序
a.sort()  # 小->大(元素排序)
print(a)
# 資料反轉
a.reverse()
print(a)
# 最大值
print("最大值: %d" % max(a))
# 最小值
print("最小值: %d" % min(a))
