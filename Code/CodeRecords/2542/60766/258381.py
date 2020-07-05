# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:25:27 2020

@author: Lenovo
"""

class Solution:
    def longestConsecutive(self,nums):
        nums = set(nums)
        res = 0
        for num in nums:
        	# 判断是否是第一个数字
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res

if __name__ == '__main__':
    num=eval(input())
    s=Solution()
    print(s.longestConsecutive(num))