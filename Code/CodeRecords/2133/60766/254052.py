# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:44:11 2020

@author: Lenovo
"""

class Solution:
    def minMoves(self, nums):
        minvalue = min(nums)
        count = 0
        for i in nums:
            count += i - minvalue
        return count

if __name__ == '__main__':
    line=input().split(',')
    nums=list(map(int, line))
    s=Solution()
    print(s.minMoves(nums))