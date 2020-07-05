def longestDist(nums):
    longest=0
    for i in range(1,len(nums)):
        curr=nums[i]-nums[i-1]
        if curr>longest: longest=curr
    return longest
nums=eval(input())
nums.sort()
print(longestDist(nums))