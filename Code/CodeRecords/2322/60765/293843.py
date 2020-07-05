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
    def isPoli(s):
        return s==s[::-1]


    # n =input()[2:-2].split('],[')a
    # target=int(input())
    L=int(input())
    R=int(input())
    res=0
    for i in range(int(math.sqrt(L)),int(math.sqrt(R))+1):
        if isPoli(str(i)) and isPoli(str(i**2)):
            res+=1
    print(res)


solve()