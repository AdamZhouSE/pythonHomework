#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input()
re=0
for i in range (0,len(s)):
    re+=int(s[i])
print(int(re//10+re%10))



