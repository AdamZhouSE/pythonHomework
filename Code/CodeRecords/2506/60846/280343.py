def func(nums):
    dp=[1]*len(nums)
    for i in range(len(nums)-2,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]: dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
#print(func([10,9,2,5,3,7,101,18]))
print(func(eval("["+input()+"]")))