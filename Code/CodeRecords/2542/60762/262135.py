#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=eval(input())
l.sort()
temp=1
for i in range (0,len(l)-1):
    for j in range (i+1,len(l)):
        if(l[j]-l[i]==j-i and j-i+1>temp):
            temp=j-i+1
print(temp)
    
        
    



