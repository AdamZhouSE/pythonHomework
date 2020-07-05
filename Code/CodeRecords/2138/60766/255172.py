# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:48:01 2020

@author: Lenovo
"""

class Solution:
    def checkSubarraySum(self, nums, k):
		# 特殊情况判断
        if len(nums) <= 1:
            return False
        n = len(nums)
        dp = [0] * n  # 定义dp
        # 自底向上
        for i in range(1,n):
            dp[i] = dp[i-1] + nums[i]
        # 遍历总和
        for i in range(n-1):
            for j in range(i+1, n):
                sums = dp[j] - dp[i] + nums[i]  # 区间差
                # 判断是否满足条件
                if k == 0:  # 考虑极端条件
                    if sums == 0:  # 满足条件就返回
                        return True
                else:
                    if sums % k == 0:  # 满足条件就返回
                        return True
        return False

if __name__ == '__main__':
    line=input().split(',')
    k=int(input())
    num=list((map(int, line)))
    s=Solution()
    print(s.checkSubarraySum(num, k))