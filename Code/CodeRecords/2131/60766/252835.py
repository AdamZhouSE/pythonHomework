# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:11:41 2020

@author: Lenovo
"""

class Solution:
    def numberOfArithmeticSlices(self, nums):
        
        # 第一次遍历
        diffs = []
        for i in range(len(nums) - 1):
            diffs.append(nums[i + 1] - nums[i])
            
        # 第二次遍历
        cons = []
        a = 1
        for i in range(1, len(diffs)):
            if diffs[i] == diffs[i - 1]:
                a += 1
            else:
                cons.append(a)
                a = 1
        cons.append(a)
        
        # 第三次遍历
        res = 0
        for num in cons:
            res += int(self.calc(num))
        return res
        
    # 用于计算cons内每个数代表的等差数列个数
    def calc(self, n):
        if n == 1:
            return 0
        n += 1
        return (n-2)*(n-1)/2
    
if __name__ == '__main__':
    num=eval(input())
    s=Solution()
    print(s.numberOfArithmeticSlices(num))