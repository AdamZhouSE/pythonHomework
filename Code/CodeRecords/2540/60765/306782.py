#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())
    # def root(i):
    #     if unions[i]<0:
    #         return i
    #     else:
    #         return root(unions[i])
    # def union(x,y):
    #     roota=root(x)
    #     rootb=root(y)
    #     # unions[roota] += unions[rootb]
    #     unions[rootb]=roota
    # def similar(c1,c2):
    #     diff=0
    #     for i in zip(c1,c2):
    #         if i[0]!=i[1]:
    #           diff+=1
    #         if diff>2:
    #             return False
    #     return True
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')
    # target=int(input())
    k, n, c = list(map(int, input().split()))
    room = [c] * (n-1)
    cows = []
    res = 0

    for i in range(k):
        cows.append(list(map(int, input().split())))
    cows.sort(key=lambda x: x[1])
    cows.sort(key=lambda x: x[0], reverse=True)
    for x, y, num in cows:
        x -= 1
        y -= 1
        if room[x:y]==[]:
            print(cows)
        if min(room[x:y]) >= num:
            for i in range(x, y):
                room[i] -= num
            res += num
    print(res)


solve()
