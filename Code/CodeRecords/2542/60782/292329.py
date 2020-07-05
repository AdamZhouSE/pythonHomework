"""
题目描述
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
"""


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    res = 0
    for i in nums:
        if i - 1 not in nums:
            y = i + 1
            while y in nums:
                y += 1
            res = max(res, y - i)
    return res


print(longestConsecutive(eval(input())))