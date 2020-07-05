#!/usr/bin/python
# -*- coding: UTF-8 -*-s=input()
l=eval(input())
le=1
for i in range (0,len(l)-1):
    re=l[i]
    for j in range (i+1,len(l)):
        if(l[j]>re):
            re=l[j]
        else:
            if(j-i>le):
                le=j-i
            break
print(le)
    







