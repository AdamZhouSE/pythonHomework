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
    n = input().split(',')
    nums=list(map(int, n[0].split()[2][1:-1].split(',')))
    k=int(n[1].split()[2])
    t = int(n[2].split()[2])
    for i in range(len(nums)):
        for j in range(i+1,min(i+k+1,len(nums))):
            if abs(nums[i]-nums[j])<=t:
                print('true')
                return 
    print('false')
solve()
