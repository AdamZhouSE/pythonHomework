"""
题目描述
    在未排序的数组中找到第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""
nums = eval(input())
k = int(input())
nums = sorted(nums, reverse=True)
print(nums[k - 1])