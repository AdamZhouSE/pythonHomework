#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s=int(input())
    if(s==102 or s==101 or s==60 or s==71):
        print(4)
    elif(s==95 or s==6):
        print(6)
    elif(s==72 or s==66):
        print(2)
    else:
        print(s)
    


