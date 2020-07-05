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
    sample=collections.Counter(input())
    num=1
    for i in range(31):
        if collections.Counter(str(num))==sample:
            print('true')
            return
        num=num<<1
    print('false')

solve()