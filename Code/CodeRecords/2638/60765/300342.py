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
            x,y,k=order[1:]

            for j in range(x,y+1):
                a[j-1]+=k

        elif order[0]==2:
            x, y = order[1:]
            print('%.4f' %(sum(a[x-1:y])/(y-x+1)))
        else:
            x, y = order[1:]
            mean=sum(a[x-1:y])/(y-x+1)
            d=[ (num-mean)**2 for num in a[x-1:y]]
            var=sum(d)/(y-x+1)
            print('%.4f'%var)






solve()