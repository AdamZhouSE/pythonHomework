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

    return max(dp)


def better_solution(n, diff):
    dp = np.zeros(20000, dtype=int)

    for i in range(0, n):
        arr[i] += 10000

    for i in range(0, n):
        prev = int(arr[i] - diff)
        if prev <= 0 or prev > 20000:
            dp[i] = 1
        else:
            dp[i] = max(dp[i], dp[prev] + 1)

    return max(dp)


print(better_solution(n, difference))
