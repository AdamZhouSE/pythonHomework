n=list(eval(input()))
nums=[1]+[i for i in n] + [1]
dp=[[0]*len(nums) for i in range(len(nums))]
for k in range(2, len(nums)):
    for left in range(0, len(nums) - k):
        right = left + k
        for i in range(left + 1,right):
            dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
print(dp[0][len(nums)-1])
    