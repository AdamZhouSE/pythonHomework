def findLongest(nums):
    dp = [1]*len(nums) #dp[i]存储以第i个元素作为结尾（包括i）时可以产生的最长子序列长度
    for i in range(1,len(nums)):
        for j in range(i):
            if(nums[i]>nums[j]):
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
print(findLongest(nums))
