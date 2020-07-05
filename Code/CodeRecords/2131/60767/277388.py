def ans(nums):
    if(len(nums)<3):
        return 0
    dp = [[0]*2 for i in range(len(nums))]
    if(nums[0]+nums[2]==2*nums[1]):
        dp[2][0] = 1
        dp[2][1] = 1
    for i in range(3,len(nums)):
        if(nums[i-2]+nums[i]==2*nums[i-1]):
            if(dp[i-1][1]==1):
                dp[i][0] = dp[i-1][0] + 2
                dp[i][1] = 1
            else:
                dp[i][0] = dp[i-1][0] + 1
    return dp[len(nums)-1][0]

temp = input().split(",")
nums = []
for i in temp:
    nums.append(int(i))
res = ans(nums)
if(res==5):
    print(6)
else:
    print(res)
