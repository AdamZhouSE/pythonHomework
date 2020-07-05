nums = list(map(int, input().split(',')))
nums = [1]+nums+[1]
length = len(nums)

dp = [[0] * length for _ in range(length)]
for k in range(2, length):
    for left in range(0, length - k):
        right  = left +k
        for i in range(left+1, right):
            dp[left][right] = max(dp[left][right], dp[i][right] + dp[left][i] + nums[left] * nums[i] * nums[right])
            dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
print(dp[0][length-1])