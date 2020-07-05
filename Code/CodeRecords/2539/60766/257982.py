# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:05 2020

@author: Lenovo
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        n=len(nums)
        max_num=nums[0]
        right=0
        for i in range(n):
            if(nums[i]>=max_num):
                max_num=nums[i]
            else:
                right=i
        left=n
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            if(nums[i]<=min_num):
                min_num=nums[i]
            else:
                left=i
        return right-left+1 if(right-left+1 >0) else 0

if __name__ == '__main__':
    num=eval(input())
    s=Solution()
    print(s.findUnsortedSubarray(num))