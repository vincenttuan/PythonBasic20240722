# 今有雞、兔同籠，上有三十五頭，下九十四足。問雉、兔各幾何？
total = 35  # 三十五頭
feet = 94  # 九十四足

rabbit = (feet - (total*2)) / (4-2)
chicken = total - rabbit

print("雞: %d 隻, 兔: %d 隻" % (chicken, rabbit))



