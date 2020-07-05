# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:39:05 2020

@author: Lenovo
"""

import collections

class Solution:
    def fourSumCount(self, A, B, C, D):
        dic = collections.Counter(a + b for a in A for b in B)
        return sum(dic.get(- c - d, 0) for c in C for d in D)

if __name__ == '__main__':
    n=[]
    for i in range(4):
        line=input().split(',')
        n.append(list(map(int, line)))
    
    s=Solution()
    print(s.fourSumCount(n[0], n[1], n[2], n[3]))