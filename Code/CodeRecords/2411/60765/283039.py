#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    if n<3:
        return
    p1=list(map(int,input().split(',')))
    p2 = list(map(int, input().split(',')))
    # serial=input().split()
    # a=list(map(int,input().split()))
    slope=(p2[1]-p1[1])/(p2[0]-p1[0])
    for i in range(n-2):
        p=list(map(int,input().split(',')))
        if (p[1]-p1[1])/(p[0]-p1[0])!=slope:
            print("False")
            return
    print('True')




solve()