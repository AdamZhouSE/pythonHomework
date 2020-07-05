def ans(nums):
    nums.sort()
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]+1):
            dp[i] =dp[i-1]+1
        else:
            dp[i] = 1
    return max(dp)

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))