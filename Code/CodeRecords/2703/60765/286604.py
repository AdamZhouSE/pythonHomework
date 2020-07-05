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
    n = input()[2:-2].split('], [')
    n = [list(map(int, s.split(','))) for s in n]
    n_size=len(n)
    union=[-1]*n_size
    for i in range(n_size):
        for j in range(n_size):
            if n[i][j]==1 and root(i)!=root(j):
                union[root(j)]=root(i)
    print(union.count(-1))


solve()