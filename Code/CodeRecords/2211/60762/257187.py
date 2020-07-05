#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=input().split(" ")
n=int(a[0])
k=int(a[1])
l=[i for i in range(n)]
ll=[i for i in range(n)]
for i in range (0,n):
    b=input().split(" ")
    l[i]=b[0]
    ll[i]=int(b[1])
for j in range (1,n):
    l[j]=l[j]+l[ll[j]-1]
for i in range (0,k):
    temp=0
    c=input()
    for j in range(0,n):
        if(str(l[j]).startswith(c)):
            temp=temp+1
    print(temp)

