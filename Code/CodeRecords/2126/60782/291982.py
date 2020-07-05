"""
题目描述
    给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
    如果有多个目标子集，返回其中任何一个均可。
"""


class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        # write your code here
        dp = [1 for i in range(len(nums))]
        nums.sort()
        # dp数组的第i个元素记录以第i个元素为尾的最长子序列长度
        for i in range(1, len(nums)):
            for j in range(0, i):
                if (nums[i] % nums[j] == 0):
                    dp[i] = max(dp[i], dp[j] + 1)
        maxp = 0
        index = -1
        # 找到全局最长子序列
        for i in range(len(dp)):
            if (dp[i] >= maxp):
                index = i
                maxp = dp[i]
        result = []
        result.append(nums[index])
        # 找出最长子序列中所有元素，往回倒，若dp值变小了则就是
        pre = index
        while (index >= 1 and pre >= 0):
            if (dp[index] != dp[pre] and nums[index] % nums[pre] == 0):
                result.append(nums[pre])
                index = pre
                pre = index - 1
            else:
                pre -= 1
        result.reverse()
        return result


s = Solution()
print(s.largestDivisibleSubset(list(map(int, input().split(",")))))

