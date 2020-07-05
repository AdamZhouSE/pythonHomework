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
    # n = input()[2:-2].split('],[')
    # n = [list(map(int, s.split(','))) for s in n]
    n = list(map(int,input()[1:-1].split(',')))
    count=collections.Counter(n)
    print(count.most_common()[:-2:-1][0])
solve()