#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    # =list(map(int,input().split()))
    # =int(input())
    n=int(input())
    p1=list(map(int,input().split(',')))
    p2 = list(map(int, input().split(',')))
    p3 = list(map(int, input().split(',')))
    if p1==p2 or p2==p3 or p3==p1 or ((p1[0]-p2[0])/(p1[1]-p2[1]))!=((p1[0]-p3[0])/(p1[1]-p3[1])):
        print('False')
        return 
    else:
        print('True')

solve()