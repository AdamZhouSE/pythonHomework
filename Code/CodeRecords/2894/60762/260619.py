#!/usr/bin/python
# -*- coding: UTF-8 -*-
len=int(input())
s=input()
re=0
if(s.count("VVV")):
    re+=1
if(s.endswith("VV")):
    re+=1
print(s.count("VK")+re,end="")
