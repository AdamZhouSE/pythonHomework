"""
题目描述
    给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
    给定 n 和 k，返回第 k 个排列。

    说明：
        给定 n 的范围是 [1, 9]。
        给定 k 的范围是[1, n!]。
"""
import math


def getPermutation(n: int, k: int) -> str:
    res, nums = "", list(range(1, n + 1))
    k -= 1
    while n:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        res += str(nums.pop(index))
    return res


print(getPermutation(int(input()), int(input())))
