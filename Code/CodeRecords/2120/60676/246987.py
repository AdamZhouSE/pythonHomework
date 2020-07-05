# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。


def fun(num):
    parts = 2
    product = max_product(num, parts)
    nex = max_product(num, parts+1)
    while nex > product:
        product = nex
        parts += 1
        nex = max_product(num, parts+1)
    return product


def max_product(num, n):
    multiplier = []
    for i in range(n):
        multiplier.append(num//n)
    for i in range(num % n):
        multiplier[i] += 1
    res = 1
    for i in range(n):
        res *= multiplier[i]
    return res


print(fun(int(input())))