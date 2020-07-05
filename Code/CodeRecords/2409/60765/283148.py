#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    # =list(map(int,input().split()))
    # =int(input())
    n=list(map(int,input().split()))
    odd=0
    even=0
    for i in n:
        if i%2==0:
            even+=1
        else :
            odd+=1
    print(min(odd,even))

solve()