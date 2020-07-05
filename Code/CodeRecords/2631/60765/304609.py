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

    # n =input()[2:-2].split('],[')
    # target=int(input())
    def searchMax(d):
        res=0
        for key,value in d.items():
            if value>res:
                res=value
        return res

    n,g=list(map(int,input().split()))
    changes=[]
    for i in range(n):
        changes.append(list(map(int,input().split())))
    changes.sort(key=lambda x:x[0])
    output=defaultdict(lambda :0)
    output[-1]=g
    maxOut=g
    res=0
    for day,cow,change in changes:
        if output[cow]==0:
            output[cow]=g
        out=output[cow]
        output[cow]+=change
        if out<maxOut:
            if out+change>=maxOut:
                res+=1
                maxOut=out+change
            else:
                pass
        else:
            maxer=searchMax(output)
            if change>0:
                maxOut+=change
                res+=1
            else:
                if maxer<maxOut:
                    maxOut=maxer
                    res+=1
                else:
                    res+=1
    print(res,end='')


solve()
