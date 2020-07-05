#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
s=input().split(" ")
n=int(s[0])
root=int(s[1])
l=[[] for i in range(n)]
re=[[] for i in range (50)]
re[0].append(root)
for g in range (0,n):
    ss=[int(x) for x in input().split(" ")]
    l[g].append(ss[0])
    l[g].append(ss[1])
    l[g].append(ss[2])
a=0
while(l.count([])!=n):
    for j in range(0,len(re[a])):
        for i in range(0,len(l)):
            if(l[i]!=[] and l[i][0] == re[a][j]):
                if (l[i][1] != 0):
                    re[a + 1].append(l[i][1])
                if (l[i][2] != 0):
                    re[a + 1].append(l[i][2])
                l[i] = []
    a=a+1
for i in range (0,len(re)):
    if(re[i]!=[]):
        print("Level %d :"%(i+1),end="")
        for j in re[i]:
            print(" %d"%j,end="")
        print()
for i in range (0,len(re)):
    if(re[i]!=[]):
        if((i+1)%2==1):
            print("Level %d from left to right:"%(i+1),end="")
            for j in re[i]:
                print(" %d"%j,end="")
            print()
        else:
            print("Level %d from right to left:" % (i+1), end="")
            for j in range (len(re[i])-1,-1,-1):
                print(" %d" % re[i][j], end="")
            print()





