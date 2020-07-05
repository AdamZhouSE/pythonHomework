# 初始值/m上取整，取这些值中最大的，从后往前数第一个即为所求
import math
l0 = input().split()
n = int(l0[0])
m = int(l0[1])
a = input().split()
for i in range(n):
    a[i] = math.ceil(int(a[i])/m)
a.reverse()
max_num = max(a)
res = a.index(max_num)
res = n-res
print (res)