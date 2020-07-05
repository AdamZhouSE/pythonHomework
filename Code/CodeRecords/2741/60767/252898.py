def findLongest(nums):
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        if(nums[i]>nums[i-1]):
            dp[i]=dp[i-1]+1
        else:
            dp[i]=0
    return max(dp)

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(findLongest(nums))