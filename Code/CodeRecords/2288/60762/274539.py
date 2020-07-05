#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input()
a=0
while(s!="0 0"):
    ss=s.split(" ")
    n=int(ss[1])
    m=int(ss[0])
    re=1
    l=[m]
    while(len(l)!=0):
        a=l[0]
        if(2*a<=n):
            re+=1
            l.append(2*a)
        if(2*a+1<=n):
            re+=1
            l.append(2*a+1)
        del l[0]
    print(re)
    s=input()


