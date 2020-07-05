#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    # n,t=list(map(int,input().split()))
    # serial=input().split()
    # a=list(map(int,input().split()))
    s1=input()

    notAllowedChar=[set() for i in range(26)]
    for i in range(1,n):
        idx=ord(s1[i])-ord('a')
        notAllowedChar[idx].add(s1[i-1])


    dp=[[0]*26 for i in range(n)]
    dp[0]=[1]*26
    for i in range(1,n):
        for j in range(26):
            for k in range(26):
                if chr(k+ord('a')) not in notAllowedChar[j]:
                    dp[i][j]+=dp[i-1][k]
    res=0
    for i in range(26):
        res+=dp[-1][i]
    print(res)






solve()