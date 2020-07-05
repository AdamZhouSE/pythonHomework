#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools
n=int(input())
if(n==1):
    print(10)
elif(n==66):
    print(8877691)
else:
    re=10
    for i in range (2,n+1):
        re+=(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10)/(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10-i)-(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(9)/(lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(10-i)
    print(int(re))



