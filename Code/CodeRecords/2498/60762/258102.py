#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=input().replace("[","").replace("]","").split(",")
l=[int(x) for x in l]
odd=[]
even=[]
re=[]
for i in range (0,len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
for i in range (0,len(even)):
    re.append(even[i])
    re.append(odd[i])
print("[",end="")
for i in range (0,len(re)):
    if(i!=len(re)-1):
        print(re[i], end=", ")
    else:
        print(re[i], end="]")

print()

