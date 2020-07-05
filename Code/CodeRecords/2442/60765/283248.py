#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
def solve():
    # =list(map(int,input().split()))
    # =int(input())
    n=input()
    l=list(map(int,n[1:-1].split(',')))
    if len(l)<2:
        print(0)
        return
    l.sort()
    res=[ l[i+1]-l[i]  for i in range(len(l)-1)]
    print(max(res))

solve()