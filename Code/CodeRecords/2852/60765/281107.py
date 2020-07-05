#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=''.join(input().split())
b=re.split(a,r'((?<=1)(?=2))|(?<=2)(?=1)')
lens=[len(str) for str in b]
maxA=0
for i in range(len(lens)-1):
    maxA=max(maxA,min(lens[i],lens[i+1]))
print(maxA)

