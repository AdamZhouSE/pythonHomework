#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
string=input()
len=len(string)
list=[]
for i in range(0,len):
    list.append(string[i:len]+str(i))
list.sort()
for i in range(0,len):
    print(int("".join(re.findall(r'\d+',list[i])))+1,end="")
    if i!=len-1:
        print(end=" ")








        
    