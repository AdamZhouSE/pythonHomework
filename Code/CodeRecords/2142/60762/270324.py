#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s = list(input())
    l = []
    a=1
    for i in range(0, len(s)):
        if (s[i] == ")"):
            l.append(s[i])
        if(s[i]=="("):
            l.append(str(a))
            a+=1
    re = "".join(l)
    ll=[]
    while(re.count(")")!=0):
        ll.append(re[re.index(")")-1])
        re=re[0:re.index(")")-1]+re[re.index(")")+1:]
    a=0
    for i in range (0,len(l)):
        if(l[i]==")"):
            l[i]=ll[a]
            a+=1
    for i in range(0, len(l)):
        print(l[i], end=" ")
    print()





