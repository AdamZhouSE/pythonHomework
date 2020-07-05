#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
string=input()
len=len(string)
lists=[[]for i in range(len)]
list=[]
for i in range(0,len):
    lists[i].append(string[i:len])
    lists[i].append(str(i+1))
dic=dict(sorted(dict(lists).items(), key=lambda x:x[0], reverse=False))
for value in dic.values():
    list.append(value)
for i in range (0,len):
    if i!=len-1:
        print(list[i], end=" ")
    else:
        print(list[i])








