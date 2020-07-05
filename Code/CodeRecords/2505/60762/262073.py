#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=[int(x) for x in input().split(",")]
s.sort()
for i in range (0,len(s)):
    if(s.count(s[i])>1):
        print(s[i])
        break
