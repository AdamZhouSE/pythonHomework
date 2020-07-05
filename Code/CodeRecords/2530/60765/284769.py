#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =list(map(int,input()[1:-1].split(',')))
    s1=list(input())
    s2 = list(input())
    allChars=collections.Counter(s2)
    res=[]
    for c in s1:
        if allChars[c]!=0:
            res.append(c)
            allChars[c]-=1

    for c in s2:
        if allChars[c] != 0:
            res.append(c)
            allChars[c] -= 1
    print(''.join(res))


solve()