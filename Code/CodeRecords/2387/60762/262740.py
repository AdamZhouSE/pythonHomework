#!/usr/bin/python
# -*- coding: UTF-8 -*-s=input()
s1=input().split(" ")
n=int(s1[0])
m=int(s1[1])
l=[int(x) for x in input().split(" ")]
for g in range (0,m):
    s=[int(x) for x in input().split(" ")]
    ll=l[s[1]:s[2]]
    if(s[0]==0):
        ll.sort()
    else:
        ll.sort(reverse=True)
    for i in range(s[1], s[2]):
        l[i] = ll[i - s[1]]
print(l[int(input())-1])
        
    










