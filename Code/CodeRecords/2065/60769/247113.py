import math


def atoi(a):
    pos = True
    res = 0
    start = 0
    if a[0] == "-":
        pos = False
        start = 1
    for i in range(start, len(a)):
        if a[i].isdigit():
            res = res * 10 + int(a[i])
        else:
            break
    if not pos:
        res = -res
    if res < -math.pow(2, 31):
        return int(-math.pow(2, 31))
    elif res > math.pow(2, 31) - 1:
        return int(math.pow(2, 31) - 1)
    return res


str = input().strip()
res = atoi(str)
print(res)
