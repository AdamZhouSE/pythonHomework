#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=list(input())
t=list(input())
temp=0
f=True
for i in range (0,len(s)):
    for j in range (temp,len(t)):
        if(t[j]==s[i]):
            temp=j+1
            break
        if(t[j]!=s[i] and j==len(t)-1):
            f=False
print(f)


