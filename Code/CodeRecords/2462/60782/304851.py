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
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left


s = Solution()
print(s.findPeakElement(list(map(int, input().split(",")))))
