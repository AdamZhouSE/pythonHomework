"""
题目描述
    给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
"""


def countNumbersWithUniqueDigits(n: int) -> int:
    counts = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    res, product = 1, 1

    # 超过10位的, 均会重复
    n = n if n <= 10 else 10
    for i in range(n):
        product *= counts[i]
        res += product

    return res


print(countNumbersWithUniqueDigits(int(input())))
