#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    # n = int(input())
    year,month,day=list(map(int,input().split('-')))
    # serial=input().split()
    # a=list(map(int,input().split()))
    daysOfMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    isLeap=False
    if year%400==0 or (year%100!=0 and year%4==0):
        isLeap=True
    if isLeap:
        daysOfMonth[1]=29
    print(daysOfMonth[:month-1]+day)
        
        





solve()