def lengthOfLIS( nums):
    if not nums:
        return 0
    n, res = len(nums), 1
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res
nums=list(map(int,input().split(',')))
print(lengthOfLIS(nums))
