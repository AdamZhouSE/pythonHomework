#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def root(i):
        if union[i]==-1:
            return i
        else:
            return root(union[i])
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    # n = input()[2:-2].split('],[')
    # n = [list(map(int, s.split(','))) for s in n]
    n=list(input())
    count=collections.Counter()
    k=int(input())
    r=l=0
    for r in range(len(n)):
        count[n[r]]+=1
        if count.most_common(1)[0][1]+k<r-l+1:
            count[n[l]]-=1
            l+=1
    print(r-l+1)



solve()