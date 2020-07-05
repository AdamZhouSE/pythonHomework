def square(m):
    str_m = str(m)
    res = 0
    for i in str_m:
        res += int(i) ** 2
    return res


def ishappy(x):
    x = square(x)
    list1 = []
    while x != 1:
        if x not in list1:
            list1.append(x)
        else:
            return False
        x = square(x)
    return True


num = int(input())
res = []
for i in range(num):
    n = int(input()) + 1
    while not ishappy(n):
        n += 1
    res.append(n)
for i in res:
    print(i)