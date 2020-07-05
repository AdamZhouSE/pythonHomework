n = int(input())
a = [int(i) for i in input().split()]


# [x,y]区间内所有元素取反的和
def f(x, y):
    r = 0
    for i in range(x, y + 1):
        r += (1 - a[i])
    return r


def s(x, y):
    r = 0
    if x == 0 and y == n - 1:
        return r
    elif x == 0 and y < n - 1:
        for i in range(y + 1, n):
            r += a[i]
        return r
    elif x > 0 and y == n - 1:
        for i in range(0, x):
            r += a[i]
        return r
    else:
        for i in range(0, x):
            r += a[i]
        for i in range(y + 1, n):
            r += a[i]
        return r


res = 0
for i in range(n):
    for j in range(i, n):
        res = max(res, f(i, j) + s(i, j))
print(res)
