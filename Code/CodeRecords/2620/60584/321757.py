nums=[int(i) for i in input().split(",")
if (len(nums)==0):
      return 0
dp=[]
dp[0]=nums[0]
for i in range(0,len(nums):
      dp[i] = Math.max(nums[i], dp[i - 1] + nums[i])
res = dp[0]
for i in range(0,len(nums)):
      res = Math.max(res,dp[i])
print(res)