#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    # n,t=list(map(int,input().split()))
    # serial=input().split()
    for i in range(n):

        a=list(input())
        all=list(set(a))
        all=''.join(sorted(all))
        minLen=len(a)
        for j in range(len(a)):
            for k in range(1,len(a)+1):
                if  all in ''.join(sorted(a[j:k])):
                    minLen=min(minLen,k-j)
        print(minLen)


solve()
