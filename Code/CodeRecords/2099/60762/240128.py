#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
a=input()
if(len(a)==1):
    print(ord(a)-ord("A")+1)
else:
    print(26*(ord(a[0])-ord("A")+1)+ord(a[1])-ord("A")+1)