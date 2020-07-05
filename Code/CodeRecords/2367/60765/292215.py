#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools


def solve():
    def getAllSubstring(str):
        n = len(str)
        res = set()
        for i in range(n):
            for j in range(i, n):
                res.add(str[i:j + 1])
        return list(res)
    def distance(p1,p2):
        pass
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n=int(input())
    if n%2==0:
        print(-1)
        return
    num=1
    while num%n!=0:
        num+=10
    print(num)
solve()