#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    s="".join([x for x in input() if x.isalpha()]).lower()
    if(s=="".join(reversed(s))):
        print("YES")
    else:
        print("NO")


