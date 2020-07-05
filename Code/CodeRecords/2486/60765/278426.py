#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    a=list(input())
    strStack=[]
    intStack=[]
    for c in a:
        if c=='['or ('a'<=c and c<='z'):
            strStack.append(c)
        elif c==']':
            token=strStack.pop()
            str=''
            while token!='[':
                str=token+str
                token = strStack.pop()
            str=intStack.pop()*str
            strStack.append(str)
        else:
            intStack.append(int(c))
    print(strStack.pop())

