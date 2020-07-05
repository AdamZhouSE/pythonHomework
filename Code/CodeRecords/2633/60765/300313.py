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
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))

    for i in range(m):
        order=list(map(int,input().split()))
        if order[0]==1:
            L,R,K,D=order[1:]
            count=0
            for j in range(L,R+1):
                a[j-1]+=(K+D*count)
                count+=1
        else:
            print(a[order[1]-1])









solve()