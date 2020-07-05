"""
题目描述
    给定一个整数 n，返回 n! 结果尾数中零的数量。
"""


def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    r = 0
    while n >= 5:
        n = n // 5
        r += n
    return r


print(trailingZeroes(int(input())))