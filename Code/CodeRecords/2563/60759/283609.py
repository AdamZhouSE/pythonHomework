from math import log


num = int(eval(input()))
l, r = 0, num
find = False
for m in range(int(log(num, 2)), 0, -1):
    l, r = 2, pow(num, 1 / m)
    while l < r:
        k = int((l + r) // 2)
        n = 1
        for i in range(m):
            n = n * k + 1
        if n == num:
            find = True
            print(int(k))
            break
        elif n < num:
            l = k + 1
        else:
            r = k
    if find:
        break
