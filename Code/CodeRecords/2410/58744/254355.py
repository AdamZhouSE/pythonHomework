import numpy as np

arr = list(eval(input()))
n = len(arr)
difference = int(input())


def solve(n, diff):
    dp = np.ones(n, dtype=int)

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] - arr[j] == diff:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n - 1]


print(solve(n, difference))
