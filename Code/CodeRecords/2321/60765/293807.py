#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())
    def list2num(l):
        res=reduce(lambda x,y:x*10+y,l)
        # print(res)
        return res
    def permutations_all(l,size):
        res=[[i] for i in l]
        for i in range(1,size):
            for j in range((size-size**i)//(1-size),(size-size**(i+1))//(1-size)):
                for k in range(len(l)):
                    res.append(res[j]+[l[k]])
        return res


    # n =input()[2:-2].split('],[')a
    # target=int(input())
    digits=list(map(int, input().split(',')))
    N=int(input())
    n=len(str(N))
    res=0
    # print(permutations_all(digits, n))

    for num in permutations_all(digits,n):
        if list2num(num)<=N:
            res+=1
    print(res)

solve()