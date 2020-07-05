#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input()
s=s.lstrip("[")
s=s.rstrip("]")
list=s.split(",")
list=[int(x) for x in list]
n=0
for i in range(0,len(list)-1):
    if(abs(list[i]-list[i+1])>n):
        n=abs(list[i]-list[i+1])
print(n)










