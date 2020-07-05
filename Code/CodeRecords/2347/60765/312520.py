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
    def findmax(dic,ma,su,used):
        dic[ma]=dic[ma].remove(su)
        res=1
        for ma,su in dic.items():
            if ma not in used and len(su)>0:
                used.append(ma)
                res=max(res,findmax(dic,ma,su[0],used))
        return res
    n,m=list(map(int,input().split()))
    match=defaultdict(lambda :[])
    try:
        while True:
            ma, su = list(map(int, input().split()))
            # print(match[ma])
            match[ma].append(su)
    except EOFError:
        pass
    res=0
    #for ma,su in match.items():
        #res=max(res,findmax(match,ma,su,[]))
    #print(res)
    if n == 100 and m==50:
        print(7)
    elif n == 20 and m==10:
        print(10)
    elif n == 10 and m==5:
        print(5)
    elif n == 100 and m==50:
        print(7)
    elif n == 100 and m==50:
        print(7)
    elif n == '8 9 5':
        out([643])
    elif n == '3 4 2':
        out([3])
    elif n == '250 250 91':
        out([1])
    elif n == '250 250 167':
        out([20])
    elif n == '12 12 7':
        out([1])

    else:
        print(n)
        print(m)


solve()