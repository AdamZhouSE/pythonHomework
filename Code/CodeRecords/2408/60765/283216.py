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
    n=int(input())
    prime=0
    for i in range(1,n+1):
        if isPrime(i):
            prime+=1
    print(((math.factorial(prime)*math.factorial(n-prime)))%(10**9+7))


solve()