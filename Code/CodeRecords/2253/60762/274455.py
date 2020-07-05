#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(" ")
n=int(s[0])
k=int(s[1])
a = input()
l = [int(x) for x in a.split(" ")]
li = []
re = 0
for i in range(0, k):
    ss = [int(x) for x in input().split(" ")]
    if (ss[0] == 1):
        le = ss[1] - 1
        r = ss[2]
        li = l[le:r]
        li.sort()
        print(li.index(ss[3]) + 1)
    elif (ss[0] == 2):
        le = ss[1] - 1
        r = ss[2]
        li = l[le:r]
        li.sort()
        print(li[ss[3] - 1])
    elif (ss[0] == 3):
        l[ss[1] - 1] = ss[2]
    elif (ss[0] == 4):
        le = ss[1] - 1
        r = ss[2]
        re = 0
        for j in range(le, r):
            if (l[j] < ss[3] and re < l[j]):
                re = l[j]
        print(re)
    else:
        le = ss[1] - 1
        r = ss[2]
        re = 10000000
        for j in range(le, r):
            if (l[j] > ss[3] and re > l[j]):
                re = l[j]
        print(re)


