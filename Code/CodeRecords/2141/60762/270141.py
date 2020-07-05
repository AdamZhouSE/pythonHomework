#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s=int(input())
    for i in range (1,s+1):
        print(bin(i).replace("0b",""),end=" ")
    print()
        


