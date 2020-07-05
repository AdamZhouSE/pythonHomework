#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    s = input()
    l = [int(x) for x in input().split(" ")]
    ll = [int(x) for x in input().split(" ")]
    re=0
    for j in range (0,len(ll)):
        for a in range (0,len(l)):
            if(l[a]==ll[j]):
                re+=1
                break
    if(re==len(ll)):
        print("Yes")
    else:
        print("No")
    
            
        










