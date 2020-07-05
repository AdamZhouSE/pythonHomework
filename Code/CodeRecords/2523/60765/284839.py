#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    n =input()[2:-2].split('],[')
    n=[ list(map(int,s.split(','))) for s in n]

    len1=len(n)
    len2=len(n[0])
    for k in range(0,len1+len2-1):
        x=max(0,len1-1-k)
        y=max(0,k-len1+1)
        a=[]
        while x<len1 and y<len2:
            a.append(n[x][y])
            x+=1
            y+=1
        a.sort(reverse=True)
        x = max(0, len1 - 1 - k)
        y = max(0, k-len1+1)
        while x < len1  and y < len2 :
            n[x][y]=a.pop()
            x += 1
            y += 1
    print(n)


solve()