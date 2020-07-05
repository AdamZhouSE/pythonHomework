def BigestMul(n):
    if n <= 3:
        return n - 1
    dp = [0] * (n + 1)
    dp[1:4] = [1, 2, 3]
    for i in range(4, n + 1):
        dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
    return dp[n]
n=int(input())
print(BigestMul(n))
