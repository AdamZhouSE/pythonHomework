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
    def dfs(level,start):
        if level==len(a):
            return 1
        count[start]-=1
        res=0
        for des in path[start]:

            if count[des]>0:
                res+=dfs(level+1,des)
        count[start]+=1
        return res
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    a=list(map(int,input().split(',')))
    res=0
    count=Counter(a)
    path={}
    for key in count:
        path[key]=[]
    for i in count:
        for j in count:
            if math.sqrt(i+j)-int(math.sqrt(i+j))==0:
                path[i].append(j)
    res=0
    for key in count:
        res+=dfs(1,key)
    print(res)




solve()