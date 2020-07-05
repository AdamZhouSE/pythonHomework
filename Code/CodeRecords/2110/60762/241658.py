#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
if(a==1):
    print(True)
while(a%2==0):
    a/=2
while(a%3==0):
    a/=3
while(a%5==0):
    a/=5
if(a==1):
    print(True)
else:
    print(False)



