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
    
    home=list(map(int,input().split(',')))
    heater = list(map(int, input().split(',')))
    dist=[]
    for h in home:
        dist.append(min([abs(he-h) for he in heater]))
    print(max(dist))
            

solve()