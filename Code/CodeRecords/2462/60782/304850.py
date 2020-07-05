"""
题目描述
    峰值元素是指其值大于左右相邻值的元素。
    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
    数组可能包含多个峰值，在这种情况下，返回第一个峰值（索引较小的那个）所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞。
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left

s = Solution()
print(s.findPeakElement(list(map(int, input().split(",")))))
