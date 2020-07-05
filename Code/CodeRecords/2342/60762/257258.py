#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    k=int(input().split(" ")[1])
    l=[int(x) for x in input().split(" ")]
    re=""
    for j in range (0,len(l),k):
        if(len(l)-j>k):
            ll=l[j:j+k]
        else:
            ll=l[j:]
        ll.sort()
        for m in range (len(ll)-1,-1,-1):
              print(str(ll[m]),end=" ")
    print()  

