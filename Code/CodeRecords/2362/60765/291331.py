#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def getAllSubstring(str):
        n = len(str)
        res = set()
        for i in range(n):
            for j in range(i, n):
                res.add(str[i:j + 1])
        return list(res)
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n=int(input())
    part=n
    sum=0
    first=True
    for i in range(n-1,0,-1):
        if ((n-i)%4)==0:
            if first:
                sum+=part
            else:
                sum-=part
            first=False
            part=i
        elif ((n-i)%4)==1:
            part*=i
        elif ((n - i) % 4) == 2:
            part=part//i
        else:
            sum+=i
    if first:
        sum += part
    else:
        sum -= part
    print(sum)


solve()