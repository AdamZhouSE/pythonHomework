nums=list(input().split(','))
nums=list(map(int,nums))
nums = sorted(nums)
dp = [[x] for x in nums]
res = []
for i in range(len(nums)):
    for j in range(i):
        if nums[i]%nums[j] == 0 and len(dp[j])+1>len(dp[i]):
            dp[i]  = dp[j]+nums[i:i+1]
    if len(dp[i])>len(res):
        res= dp[i]
print(res)