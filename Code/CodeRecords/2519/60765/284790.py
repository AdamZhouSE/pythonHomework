#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    n =list(map(int,input()[1:-1].split(',')))
    for i in range(len(n)-3,-1,-1):
        if n[i]+n[i+1]>n[i+2]:
            print(n[i]+n[i+1]+n[i+2])
            return 
    print(0)



solve()