# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:37:03 2020

@author: Lenovo
"""

class Solution:
    def reverse(self, x):
        str_num = str(x)[::-1]
        if str_num.endswith('-'):
            str_num = '-' + str_num[:-1]
            return int(str_num) if int(str_num) >= -2**31 else 0
        return int(str_num) if int(str_num) <= 2**31 - 1 else 0

if __name__ == '__main__':
    n=int(input())
    s=Solution()
    print(s.reverse(n))