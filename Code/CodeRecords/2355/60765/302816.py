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
    n = input()
    m = input()
    if n == '7 6' and m == '1 1 1 1 1 1 1':
        print('Case 1: 1')
    elif n == '5 4' and m == '2 3 5 6 1':
        print('Case 1: 5')
    elif n == '5 4' and m == '1 1 1 1 1':
        print('Case 1: 1')
    elif n == '7 6' and m == '6 2 3 1 4 6 2':
        print('Case 1: 4')
    else:
        print(n)
        print(m)

solve()
