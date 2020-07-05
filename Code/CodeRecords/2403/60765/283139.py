#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    # =list(map(int,input().split()))
    # =int(input())
    candy=int(input())
    people=int(input())
    count=1
    res=[0]*people
    while True:
        for i in range(people):
            if candy>count:
                res[i]+=count
                candy -= count
                count+=1
                
            else:
                res[i]+=candy
                print(res)
                return







solve()