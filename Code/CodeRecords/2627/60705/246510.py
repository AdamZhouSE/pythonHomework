import math

n = int(input())
for i in range(0, n):
    a = list(map(int, input().split(" ")))
    p = a[0]  # 长度
    s = a[1]  # 面积
    m1 = p/12  # 长度足够时的最大边长
    m2 = math.sqrt(s/5)  # 面积足够时的最大边长
    print(min(m1, m2)**3)