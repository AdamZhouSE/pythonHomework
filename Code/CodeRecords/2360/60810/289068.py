'''
给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。
'''

import math

def numSquarePerms(A):
    nums = A
    nums.sort()
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            #去重
            if i and nums[i]==nums[i+-1]:
                continue
            if not tmp or math.sqrt(tmp[-1] + nums[i])%1==0:
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
    backtrack(nums, [])
    return len(res)

inp = input()
A = inp.split(',')
A = list(map(int, A))
res = int(numSquarePerms(A))
print(res)