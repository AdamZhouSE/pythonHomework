#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input()
s=s.lstrip("[")
s=s.rstrip("]")
list=s.split(",")
if(len(list)>=2):
    list = [int(x) for x in list]
    list.sort()
    n = 0
    for i in range(0, len(list) - 1):
        if (list[i+1] - list[i]) > n:
            n = list[i+1] - list[i]
    print(n)
else:
    print(0)
   










