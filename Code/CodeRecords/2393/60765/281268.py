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
        n2=input()
        a1=list(map(int,input().split()))
        a2=list(map(int,input().split()))
        count=0
        for j in a1:
            for k in a2:
                if j**k>k**j:
                    count+=1
        print(count)


solve()
