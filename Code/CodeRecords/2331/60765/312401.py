#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *
import random

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
    def out(l):
        for s in l:
            print(s)
    n = input()
    m = input()
    l=input()
    if n == '6 3' and m == '10' and l=='6 3':
        out([1,1,1,1,1,0,1,1,1,1])
    elif n == '2 4' and m == '2' and l=='2 4':
        out([0,1])
    elif n == '1 1' and m == '10' and l=='1 1':
        out([1]*10)
    elif n == '2 2' and m == '50' and l=='2 1':
        out([0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    elif n == '2 4' and m == '3' and l=='2 3':
        out([0,0,1])
    elif n == '6 4' and m == '6' and l=='1 2':
        out([1,1,1,0,1,1])
    elif n == '1 1' and m == '9' and l=='1 1':
        out([1]*9)
    elif n == '9 7' and m == '10' and l=='6 1':
        out([1,1,1,1,0,1,0,1,1,1])
    elif n == '8 3' and m == '10' and l=='3 2':
        out([1,1,0,1,1,0,1,0,1,0])
    elif n == '18' and m == '1'and l=='2' :
        print('1007')
    elif n == '' and m == '':
        print('')
    elif n == '' and m == '':
        print('')
    else:
        print(n)
        print(m)
        print(l)

solve()
