#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=input()
b=re.split(r'((?<=1)\s(?=2))|(?<=2)\s(?=1)',a)
lens=[str.count('1')+str.count('2') for str in b if str is not None and str!=' ']
maxA=0
for i in range(len(lens)-1):
    maxA=max(maxA,min(lens[i],lens[i+1]))
print(maxA*2)

