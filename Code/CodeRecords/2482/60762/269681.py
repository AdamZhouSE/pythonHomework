#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    a =int(input())
    b=int(input())
    if(len(str(a/b))>10):
        print("%d.(%s)"%(a//b,str(a/b)[2]))
    elif(a%b==0):
        print(int(a/b))
    else:
        print(a/b)

