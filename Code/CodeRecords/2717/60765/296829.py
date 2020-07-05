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
    def root(i):
        if unions[i]<0:
            return i
        else:
            return root(unions[i])
    def union(x,y):
        roota=root(x)
        rootb=root(y)
        unions[roota] += unions[rootb]
        unions[rootb]=roota
    def char2int(c):
        return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    equations=input()[2:-2].split('","')
    #print(equations)
    unions=[-1]*26
    for equa in equations:
        a,b=equa[0],equa[3]
        if equa[1]=='=' and root(char2int(a))!=root(char2int(b)):
            union(char2int(a),char2int(b))
        elif equa[1]=='!' and root(char2int(a))==root(char2int(b)):
            print('false')
            return 
    print('true')
    







solve()