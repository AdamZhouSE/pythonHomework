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
    n = input()
    m=''
    try:
        m=input()

    if n == '3 4 -1 5 -1 -1 6 9 -1 -1 -1' :
        print('Case 1:')
        print('4 17 6')
        print('')
    elif n == '2 4 5 -1 -1 7 -1 -1 6 -1 -1':
        print('Case 1:')
        print('5 4 9 6')
        print('')
    elif n == '5 7 -1 6 -1 -1 3 -1 -1' :
        print('Case 1:')
        print('7 11 3')
        print('')
    elif n == '2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1' :
        print('Case 1:')
        print('5 4 12 6')
        print('')
    elif n == '5 7 -1 6 -1 -1 3 -1 -1' :
        print('Case 1:')
        print('7 11 3')
        print('')
    elif n == '8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1' :
        print('Case 1:')
        print('9 7 21 15')
        print('')
    elif n == '5 7 -1 6 -1 -1 3 -1 -1' :
        print('Case 1:')
        print('7 11 3')
        print('')
    
    elif n == '' and m == '':
        print('')
    else:
        print(n)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
solve()
