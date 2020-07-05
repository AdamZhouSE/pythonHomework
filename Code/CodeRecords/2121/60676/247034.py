# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。


def fun(n):
    if n == 1:
        return 10
    res = 9
    for i in range(n-1):
        res *= 9 - i
    return res + fun(n-1)


print(fun(int(input())))