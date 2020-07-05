# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:03:48 2020

@author: Lenovo
"""

import math

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    count=0
    for ev in num:
        if ev<0:
            continue
        if math.sqrt(ev)%1!=0:
            count=max(count, ev)
    if count==0:
        print(-1)
    else:
        print(count)