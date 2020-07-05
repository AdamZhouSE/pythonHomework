#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    # n = input()[2:-2].split('],[')
    # n = [list(map(int, s.split(','))) for s in n]
    n = list(map(int,input()[1:-1].split(',')))
    n_sorted=sorted(n)
    res=0
    count=[0]*(len(n)+1)
    for i,j in zip(n,n_sorted):
        count[i]+=1
        count[j]-=1
        if all(i==0 for i in count):
            res+=1
    print(res)
solve()