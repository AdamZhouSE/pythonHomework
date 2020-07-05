#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n = input()[2:-2].split('],[')
    n = [list(map(int, s.split(','))) for s in n]
    vegan=int(input())
    maxPri=int(input())
    maxDis=int(input())
    n.sort(reverse=True,key=lambda x:x[0])
    n.sort(reverse=True, key=lambda x: x[1])
    res=[i[0]   for i in n if i[2]>=vegan and i[3]<=maxPri and i[4]<=maxDis]
    print(res)
    


solve()