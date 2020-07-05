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
    # target=int(input())
    str=list(input())
    strList=[str]
    for i in range(len(str)-1):
        str=str[1:]+str[0]
        strList.append(str)
    strList.sort()
    
    res=[c[-1] for c in strList]
    print(''.join(res))


solve()