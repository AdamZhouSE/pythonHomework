#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(",")
k=input()
if(s.count(k)!=0):
    print("[%d, %d]"%(s.index(k),s.index(k)+s.count(k)-1))
else:
    print("[-1, -1]")







