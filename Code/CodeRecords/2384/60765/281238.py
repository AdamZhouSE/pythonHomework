#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    # n,t=list(map(int,input().split()))
    # serial=input().split()
    for i in range(n):
        n2=int(input())
        a=list(map(int,input().split()))
        b=[0]*len(a)
        for num in a:
            if num>=0 and num<=len(a):
                b[num-1]=1
        for j in range(len(b)):
            if b[j]!=1:
                print(j+1)
                return
        if len(b)==0:
            print(1)
            return 
        print(len(a)+1)

solve()