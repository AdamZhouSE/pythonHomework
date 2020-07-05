#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=input()
b=input()
re=0
for i in range (0,len(a)-len(b)+1):
    if(a[i:i+len(b)]==b):
        re+=1
print(re,end="")












