#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
l=[]
for i in range (0,n):
    s=[int(x) for x in input().split(" ")]
    if(s[0]==1):
        l.append(s[1])
    elif(s[0]==2):
        for j in range (0,len(l)):
            if(l[j]==s[1]):
                del l[j]
                break
    elif(s[0]==3):
        ll=[-50]
        for j in range (0,len(l)):
            ll.append(l[j])
        ll.sort()
        for j in range (1,len(ll)):
            if(ll[j]==s[1]):
                print(j)
                break
    elif(s[0]==4):
        lll= [-50]
        for j in range(0, len(l)):
            lll.append(l[j])
        lll.sort()
        print(lll[s[1]])
    elif(s[0]==5):
        re=0
        for m in range (0,len(l)):
            if(l[m]<s[1] and re<l[m]):
                re=l[m]
        print(re)
    else:
        ree=100000000
        for m in range (0,len(l)):
            if(l[m]>s[1] and ree>l[m]):
                ree=l[m]
        print(ree)


