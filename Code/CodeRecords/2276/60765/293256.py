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
    if C*R==1:
        print(res)
        return

    while True:
        for i in itertools.count(1,2):
            steps=[(0,1)]*i+[(1,0)]*i+[(0,-1)]*(i+1)+[(-1,0)]*(i+1)
            for dis_r,dis_c in steps:
                r0+=dis_r
                c0+=dis_c
                if (0<=r0<R) and (0<=c0<C):
                    res.append([r0,c0])
                    if len(res)>=(C*R):
                        print(res)
                        return


solve()