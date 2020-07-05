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

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n=int(input())
    spans=[]
    for _ in range(n):
        spans.append(list(map(int,input().split())))
    spans.sort(key=lambda x:x[0])
    start=spans[0][0]
    end=spans[0][1]

    for span in spans:
        if span[0]<=end:
            end=span[1]
        elif span[0]>end:
            print('%d %d'%(start,end))
            start=span[0]
            end=span[1]
    print('%d %d' % (start, end))





solve()