#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    target=int(input())
    position=list(map(int,input()[1:-1].split(',')))
    speed = list(map(int, input()[1:-1].split(',')))
    res=len(position)
    for i in range(len(position)-1):
        if (target-position[i])/speed[i]<=(target-position[i+1])/speed[i+1]:
            res-=1
    print(res)
solve()