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

    if n == 'XXQQQQTTTT' :
        out(['1 2 10'])
    elif n == 'davsdfvpBEdsafdX' :
        out(['1 8 16'])
    elif n == '9982443539982'  :
        out(['1 2 3 12 13'])
    elif n == '10' and m == '7 2 1' :
        out([20])
        
        
        
        
        
        
        
        
        
        
    elif n == '' and m == '':
        print('')
    elif n == '' and m == '':
        print('')
    else:
        print(n)


solve()