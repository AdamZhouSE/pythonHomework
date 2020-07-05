"""
题目描述
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
    如果不存在符合条件的连续子数组，返回 0。
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        minLen = len(nums) + 1
        for i, _ in enumerate(nums):
            total = 0
            for j, tmp in enumerate(nums[i:]):
                total += tmp
                if total >= s:
                    minLen = min(minLen, j + 1)

        # 如果没有发生任何替换, 说明不存在
        if minLen == len(nums) + 1:
            return 0

        return minLen


s = Solution()
print(s.minSubArrayLen(int(input()), list(map(int, input().split(",")))))
