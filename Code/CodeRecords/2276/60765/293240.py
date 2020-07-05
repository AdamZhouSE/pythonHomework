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

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    R=int(input())
    C=int(input())
    r0=int(input())
    c0=int(input())
    res=[[r0,c0]]
    r=c=0
    while True:
        for i in itertools.count(1,2):
            steps=[(0,1)]*i+[(1,0)]*i+[(0,-1)]*(i+1)+[(-1,0)]*(i+1)
            for dis_r,dis_c in steps:
                r+=dis_r
                c+=dis_c
                if (0<=r<R) and (0<=c<C):
                    res.append([r,c])
                    if len(res)>=(C*R):
                        print(res)
                        return


solve()