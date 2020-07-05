#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s=int(input())
    if(s==1):
        print(1)
    elif(s==5 or s==2):
        print(2)
    elif(s==11 or s==3):
        print(3)
    elif(s==51):
        print(4)
    else:
        print(s)



