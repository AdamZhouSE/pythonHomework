class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        length = 1
        mmax = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                mmax = max(length, mmax)
                length = 1
        return max(length, mmax)


inputStr = input().strip()
strs = inputStr.replace("[","").replace("]","").split(",")
nums = []
for item in strs:
    nums.append(int(item))
s = Solution()
print(s.findLengthOfLCIS(nums))