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
    def f(drum):
        last=-1
        count=0
        res=0
        for i in drum:
            if i==last:
                res=max(count,res)
                count=1
            else:
                count+=1
            last=i
        res = max(count, res)
        return res
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n,m=list(map(int,input().split()))
    orders=[]
    drum=[0]*n
    for i in range(m):
        orders.append(int(input()))
    for order in orders:
        drum[order-1]=drum[order-1]^1
        print(f(drum))





solve()