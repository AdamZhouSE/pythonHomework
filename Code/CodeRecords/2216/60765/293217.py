#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools
from functools import *


def solve():
    def lcm(a, b):
        x, y = a, b
        while b:
            a, b = b, a % b
        return x * y // a

    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    def add(a1,a2):
        a_lcm=lcm(a1[1],a2[1])
        divide=a1[0]*a_lcm//a1[1]+a2[0]*a_lcm//a2[1]
        a_gcd=gcd(a_lcm,abs(divide))
        a_lcm=a_lcm//a_gcd
        divide=divide//a_gcd

        return [divide,a_lcm]
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    string=input()
    addends=re.findall(r'[-+]?\d+/\d+',string)
    addends=[list(map(int,a.split('/'))) for a in addends]
    res=reduce(add,addends)
    print(str(res[0])+'/'+str(res[1]))


solve()