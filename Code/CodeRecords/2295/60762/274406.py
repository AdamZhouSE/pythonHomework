#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
s=input().split(" ")
n=int(s[0])
root=int(s[1])
l=[[] for i in range (20)]
for i in range (0,n):
    ss=[int(x) for x in input().split(" ")]
    l[i].append(ss[0])
    l[i].append(ss[1])
    l[i].append(ss[2])
sss=[int(x) for x in input().split(" ")]
o1=sss[0]
o2=sss[1]
l1=[]
l2=[]
while(o1!=root):
    for i in range(0, n):
        temp=0
        for j in range(1, 3):
            if (l[i][j] == o1):
                o1 =l[i][0]
                l1.append(l[i][0])
                temp=1
                break
        if(temp==1):
            break
while(o2!=root):
    for i in range(0, n):
        temp=0
        for j in range(1, 3):
            if (l[i][j] == o2):
                o2 =l[i][0]
                l2.append(l[i][0])
                temp=1
                break
        if(temp==1):
            break
if(l1[0]==sss[1]):
    print(sss[1])
elif(l2[0]==sss[0]):
    print(sss[0])
else:
    for i in range(0, len(l1)):
        if (l2.count(l1[i]) == 1):
            print(l1[i])
            break

