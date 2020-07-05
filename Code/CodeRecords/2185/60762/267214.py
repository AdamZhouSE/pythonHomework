#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    re=0
    a=0
    while(re<n):
        a+=1
        re+=math.pow(2,a)
    n=n-re+math.pow(2,a)
    l=list(bin(int(n)-1).replace("0b",""))
    re=[]
    for i in range (0,a-len(l)):
        re.append("4")
    for i in range (0,len(l)):
        if(l[i]=="0"):
            re.append("4")
        else:
            re.append("7")
    print("".join(re))