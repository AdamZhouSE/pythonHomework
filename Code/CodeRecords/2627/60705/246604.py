import math

n = int(input())
for i in range(0, n):
    a = list(map(int, input().split(" ")))
    p = a[0]  # 长度
    s = a[1]  # 面积
    x = 0
    res = []
    while x < p/4:
        y = 0
        while y < p/4:
            z = 0
            while z < p/4:
                if 4*(x+y+z) == p and 2*(x*y+x*z+y*z) == s:
                    res.append(x*y*z)
                z += 1/100
            y += 1/100
        x += 1/100
    
    maximum = res[0]
    for item in res:
        if item > maximum:
            maximum = item
    print(maximum)

