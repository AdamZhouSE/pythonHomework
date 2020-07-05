"""
题目描述
    给定一个未经排序的整数数组，找到最长且连续的的递增序列。
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        m = 0
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if count > m:
                    m = count
                count = 1
        return max(m, count)


s = Solution()
print(s.findLengthOfLCIS(eval(input())))