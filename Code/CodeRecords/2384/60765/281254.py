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
        for j in range(1,n2+2):
            if j not in a:
                print(j)
                break

solve()
