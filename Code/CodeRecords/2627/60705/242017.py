import math

n = int(input())
for i in range(0, n):
    a = list(map(int, input().split(" ")))
    p = a[0]
    s = a[1]
    m1 = p/12
    m2 = math.sqrt(s/6)
    print(min(m1, m2)**3)
