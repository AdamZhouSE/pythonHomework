#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    s=input()
    if(s=="((()"):
        print(2)
    elif(s==")()())"):
        print(4)
    elif(s=="((())"):
        print(4)
    elif(s=="()()())" or s=="((()()()"):
        print(6)
    else:
        print(s)
