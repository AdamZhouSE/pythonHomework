"""
题目描述
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
"""
nums = list(map(int, input().split(",")))
cur = nums[0]
length = 0
for i in range(0, len(nums) - 1):
    if nums[i] >= cur:
        length += 1
        cur = nums[i]
    else:
        length = 0
        cur = nums[i]
print(length)