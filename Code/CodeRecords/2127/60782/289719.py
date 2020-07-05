"""
题目描述
    你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
"""
"""
输入描述
    略。
"""
"""
输出描述
    略。
"""


# def power(x, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return x % 1337
#     return power(x % 1337, n / 2) * power(x % 1337, n - n / 2) % 1337
#
#
# def super_power(a, b):
#     res = 1
#     for i in range(len(b)):
#         res = power(res, 10) * power(a, b[i]) % 1337
#     return res


def super_power(a, b) -> int:
    r = 1
    for _b in b:
        r = pow(r, 10, 1337) * pow(a, _b, 1337) % 1337
    return r


a = int(input())
b = list(map(int, input().split(",")))
# print(a)
# print(b)
print(super_power(a, b))
