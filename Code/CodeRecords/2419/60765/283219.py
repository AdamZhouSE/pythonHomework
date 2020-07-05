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
    n=list(map(int,list(input())))
    p=1
    a=0
    for i in n: 
        a+=i
        p*=i
    print(p-a)


solve()