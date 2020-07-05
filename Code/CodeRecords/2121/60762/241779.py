#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools
n=int(input())
if(n==1):
    print(10)
else:
    if(n>10):
        n=10
    re=10
    for i in range (2,n+1):
        re+=(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10)/(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10-i)-(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(9)/(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10-i)
    print(int(re))



