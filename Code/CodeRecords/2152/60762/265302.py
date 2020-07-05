#!/usr/bin/python
# -*- coding: UTF-8 -*-
#关键l=a!!!!
n=int(input())
a=[0]
b=[0]
a.extend([int(x) for x in input().split(" ")])
b.extend([int(x) for x in input().split(" ")])
l=[0]
for i in range (1,n+1):
    l.append(a[i])
for i in range (1,n+1):
    ll=[0]
    for j in range (1,n+1):
        ll.append(j)
    m = i
    ll[i] = 0
    while (ll[b[m]] != 0):
        l[i] += a[b[m]]
        ll[b[m]] = 0
        m = b[m]
    print(l[i])

    