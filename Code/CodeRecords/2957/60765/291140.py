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
    str=input()
    strList=getAllSubstring(str)
    res=0
    for s in strList:
        switch=True
        last=s[0]
        res+=1
        for c in s:
            if c != last:
                if switch:
                    switch=False
                else:
                    res-=1
                    break
            last=c
    print(res)

solve()