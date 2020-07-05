#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(" ")
n=int(s[0])
k=int(s[1])
l=[]
s=input().split(" ")
for i in range(0,n):
    l.append(int(s[i]))
li = []
re = 0
for i in range(0, k):
    ss=input().split(" ")
    if (int(ss[0]) == 1):
        le = int(ss[1])- 1
        r = int(ss[2])
        li = l[le:r]
        li.sort()
        print(li.index(int(ss[3])) +1)
    elif (int(ss[0]) == 2):
        le = int(ss[1]) - 1
        r = int(ss[2])
        li = l[le:r]
        li.sort()
        print(li[int(ss[3]) - 1])
    elif (int(ss[0]) == 3):
        l[int(ss[1]) - 1] = int(ss[2])
    elif (int(ss[0]) == 4):
        le = int(ss[1]) - 1
        r = int(ss[2])
        re = 0
        for j in range(le, r):
            if (l[j] < int(ss[3]) and re < l[j]):
                re = l[j]
        print(re)
    else:
        le = int(ss[1]) - 1
        r = int(ss[2])
        re = 10000000
        for j in range(le, r):
            if (l[j] > int(ss[3]) and re > l[j]):
                re = l[j]
        print(re)



