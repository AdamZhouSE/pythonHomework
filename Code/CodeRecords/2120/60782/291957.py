"""
题目描述
    给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。
    返回你可以获得的最大乘积。
"""


def integerBreak(n: int) -> int:
    if n <= 3:
        return n - 1
    dp = [0] * (n + 1)
    dp[1:4] = [1, 2, 3]
    for i in range(4, n + 1):
        dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
    return dp[n]


print(integerBreak(int(input())))
