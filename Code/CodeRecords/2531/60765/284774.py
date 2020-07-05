#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =list(map(int,input()[1:-1].split(',')))
    s1=list(input())
    allChars=collections.Counter(s1)
    s1.sort(reverse=True,key=lambda x:allChars[x])
    print(''.join(s1))


solve()