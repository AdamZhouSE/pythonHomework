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
        count=[0]*26
        a=list(input())
        for c in a:
            count[c-'a']+=1
        i=0
        j=len(a)-1
        while count[a[i]-'a']>1:
            i+=1
            count[a[i] - 'a']-=1

        while count[a[j] - 'a'] > 1:
            j -= 1
            count[a[j] - 'a'] -= 1
        print(i-j+1)


solve()
