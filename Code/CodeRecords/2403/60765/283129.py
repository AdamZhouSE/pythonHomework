#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    candy,people =list(map(int,input().split()))
    count=1
    res=[0]*people
    while True:
        for i in range(people):
            if candy>count:
                res[i]+=count
                count+=1
                candy-=count
            else:
                res[i]+=candy
                print(res)
                return







solve()