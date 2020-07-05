#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=input().replace("[","").replace("]","").split(",")
l=[int(x) for x in l]
re=0
for i in range (0,len(l)-1):
    for j in range (i+1,len(l)):
        if(l[i]>2*l[j]):
            re+=1
print(re)


