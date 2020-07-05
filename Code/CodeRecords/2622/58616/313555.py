# LeetCode 169
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[int(len(nums)/2)]

nums = input().split(',')
s = Solution()
print(s.majorityElement(nums))