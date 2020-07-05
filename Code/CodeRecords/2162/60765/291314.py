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
    x=int(input())
    y=int(input())
    res=x**y
    print('%.5f' %res)


solve()