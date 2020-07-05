#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input()
s=s.lstrip("[")
s=s.rstrip("]")
list=s.split(",")
list.sort()
print("[",end="")
for i in range(0,len(list)):
    if(i!=len(list)-1):
        print(list[i], end=", ")
    else:
        print(list[i], end="]")
print("")












