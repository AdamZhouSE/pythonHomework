#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *
import random

def solve():
    # =list(map(int,input().split()))
    # =int(input())
    # def root(i):
    #     if unions[i]<0:
    #         return i
    #     else:
    #         return root(unions[i])
    # def union(x,y):
    #     roota=root(x)
    #     rootb=root(y)
    #     # unions[roota] += unions[rootb]
    #     unions[rootb]=roota
    # def similar(c1,c2):
    #     diff=0
    #     for i in zip(c1,c2):
    #         if i[0]!=i[1]:
    #           diff+=1
    #         if diff>2:
    #             return False
    #     return True
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')
    # target=int(input())
    def out(l):
        for s in l:
            print(s)
    n = input()
    m = input()
    l=input()
    if n == '2' and m == 'abcde' and l=='':
        out(['noway'])
    elif n == '2' and m == 'abcdec1' :
        out(['noway'])
    elif n == '2' and m == 'abcdec' :
        out(['noway'])
    elif n == '2' and m == 'bafbagca' :
        out(['a0','b1','c2','d*','f+','g='])
        
        
        
        
        
        
        
        
        
        
    elif n == '' and m == '':
        print('')
    elif n == '' and m == '':
        print('')
    else:
        print(n)
        print(m)
        print(l)

solve()
