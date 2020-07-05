def maxCoins(k):
    nums = [1]
    for i in k:
        nums.append(i)
    nums.append(1)
    n = len(nums)

    dp = [[0] * n for _ in range(n)]

    for left in range(n - 2, -1, -1):
        for right in range(left + 2, n):
            dp[left][right] = max(
                nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right))

    return dp[0][n - 1]

k = eval(input())
print(maxCoins(k))
