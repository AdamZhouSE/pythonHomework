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
    add1=list(map(int,input().split(',')))
    add2=list(map(int,input().split(',')))
    n1=n2=0
    for i in add1:
        n1=n1*(-2)+i
    for i in add2:
        n2=n2*(-2)+i
    res=n1+n2
    resList=[]
    while res!=0:
        if res%-2!=0:
            resList.append(1)
            res=math.ceil(res/-2)
        else:
            res=res//-2
            resList.append(0)
    resList.reverse()
    print(resList)


solve()