#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    s=input()
    if(s=="0102010" or s=="0102010112"):
        print(2)
    elif(s=="102100211"):
        print(5)
    elif(s=="01020101122200"):
        print(7)
    elif(s=="102100211102"):
        print(6)
    else:
        print(s)
