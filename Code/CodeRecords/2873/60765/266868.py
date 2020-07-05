#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=input()
serial=list(map(int,input().split()))
code_possible=list(map(int,input().split()))
code=[]
for num in serial:
    if num in code_possible:
        code.append(str(num))

print(' '.join(code))