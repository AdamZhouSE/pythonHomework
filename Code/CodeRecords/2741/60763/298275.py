def findLengthOfLCIS(nums):
    ans = anchor = 0
    for i in range(len(nums)):
        if i and nums[i - 1] >= nums[i]: anchor = i
        ans = max(ans, i - anchor + 1)
    return ans

s = eval(input())
print(findLengthOfLCIS(s))