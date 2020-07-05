#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools


def solve():

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    res = int(input())
    resList = []
    while res != 0:
        if res % -2 != 0:
            resList.append('1')
            res = math.ceil(res / -2)
        else:
            res = res // -2
            resList.append('0')
    resList.reverse()
    print(''.join(resList))
solve()