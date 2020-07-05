# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:36:26 2020

@author: Lenovo
"""

from typing import List


class Solution:
    def maxProfit(self, prices):
        #print(prices)
        profit = 0
        pr=[]
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
                pr.append(i)
        #print(pr)
        res=''
        for i in range(len(prices)):
            if (not i in pr) and (i+1 in pr):
                res=res+'('+str(i)+' '
            elif (i in pr) and (not i+1 in pr):
                res=res+str(i)+') '
            else:
                continue
                
        print(res[:-1])


if __name__ == '__main__':
    s=Solution()
    n=int(input())
    num=[]
    for i in range(n):
        line=input()
        line=input().split()
        num=list(map(int, line))
        s.maxProfit(num)