#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=input()
#serial=input().split()
a=list(map(int,input().split()))
num_0=a.count(0)
num_5=a.count(5)
result='5'*(9*(num_5//9))
if result!='':
    result+='0'*num_0
elif num_0>0:
    result='0'
else:
    result='-1'
print(result)