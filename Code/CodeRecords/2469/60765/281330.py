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

        a=list(input())
        count=dict.fromkeys(list(set(a)),0)

        for c in a:
            count[c]+=1
        i=0
        j=len(a)-1
        while count[a[i]]>1:
            count[a[i]] -= 1
            i+=1


        while count[a[j] ] > 1:
            count[a[j]] -= 1
            j -= 1

        print(j-i+1)


solve()
