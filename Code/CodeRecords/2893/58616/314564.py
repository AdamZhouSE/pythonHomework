# LeetCode 137
class Solution:
    def singleNumber(self, nums):
        nums.sort()
        nums.append(0)
        nums.append(0)
        for i in range(0,len(nums),3):
            if nums[i]!=nums[i+2]:
                return nums[i]


nums = eval(input())
s = Solution()
print(s.singleNumber(nums))