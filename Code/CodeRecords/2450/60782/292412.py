"""
题目描述
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
"""


def solution(nums, target):
    # 如果列表长度小于2，则直接结束
    if len(nums) < 2:
        return
    # 两次循环列表，分别对列表中的所有可能的数字进行相加
    # 循环两次列表对应的时间复杂度为O(n²)
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


answer = solution(list(map(int, input().split(","))), int(input()))
if answer == None:
    answer = [-1, -1]
print(answer)
