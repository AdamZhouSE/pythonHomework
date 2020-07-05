#!/usr/bin/python
# -*- coding: UTF-8 -*-
re=0
for i in range (0,int(input())+1):
    if(str(i).count("1")!=0):
        re+=str(i).count("1")
print(re)



