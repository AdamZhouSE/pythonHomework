# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:14:56 2020

@author: Lenovo
"""

class Solution:
    def sortArrayByParity(self, A):
        return [a for a in A if not a % 2]+[a for a in A if a % 2]


if __name__ == '__main__':
    s=Solution()
    num=eval(input())
    print(s.sortArrayByParity(num))