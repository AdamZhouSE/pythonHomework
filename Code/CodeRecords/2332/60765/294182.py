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
    def f(target,level):
        if target==0:
            return 0
        if target==1:
            return cost[level]
        diff=target%x
        return min(diff*cost[level]+f(target//x,level+1),(x-diff)*cost[level]+f(target//x+1,level+1))

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    x=int(input())
    res=0
    target=int(input())
    
    cost=[2]+list(range(1,100))
    res=f(target,0)-1
    print(res)





solve()