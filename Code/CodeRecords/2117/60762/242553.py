#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
s=""
for i in range (0,n):
    if(i%2==0):
        s=s+"1"
    else:
        s=s+"0"
for i in range (3,n+1):
    for j in range (i-1,n,i):
        if(s[j]=="1"):
            s=s[:j-1]+"0"+s[j+1:]
        else:
            s=s[:j-1]+"1"+s[j+1:]
print(s.count("1"))