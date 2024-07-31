# 利用 for 求質數
n = 27
for i in range(2, n):
    print("%d %% %d = %d" % (n, i, (n % i)))

