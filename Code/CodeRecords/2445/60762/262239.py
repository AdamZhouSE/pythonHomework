#!/usr/bin/python
# -*- coding: UTF-8 -*-
#为什么需要strip
s=input().replace("s","").replace("t","").replace("=","").split(",")
l=list(s[0].strip())
ll=list(s[1].strip())
l.sort()
ll.sort()
if(l==ll):
    print("true")
else:
    print("false")







