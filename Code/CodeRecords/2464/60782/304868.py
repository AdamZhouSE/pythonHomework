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
        li = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) + 1):
                # print(nums[i:j])
                if sum(nums[i:j]) >= s:
                    li.append(len(nums[i:j]))
        # print(li)
        if len(li) == 0:
            return 0
        else:
            return min(li)


s = Solution()
print(s.minSubArrayLen(int(input()), list(map(int, input().split(",")))))