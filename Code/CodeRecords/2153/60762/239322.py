#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
a=input()
if(a[0]=="-"):
    re="-"
    a=a[1:]
else:
    re=""
if(a.endswith("0")):
    for i in range(len(a)-2,-1,-1):
        re=re+a[i]
else:
    for i in range(len(a)-1,-1,-1):
        re=re+a[i]
print(re)






