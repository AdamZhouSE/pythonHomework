#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=[int(x) for x in input().split(",")]
if(s[0]>s[1]):
    print(0)
else:
    re=0
    for i in range (1,len(s)-1):
        if(s[i-1]<s[i] and s[i]>s[i+1]):
            re=1
            print(i)
            break
    if(re==0 and s[len(s)-2]<s[len(s)-1]):
        print(len(s)-1)
        



