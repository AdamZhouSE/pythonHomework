#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=input()
b=input()
la=len(a)
lb=len(b)
len=la
jinwei=0
r1=0
re=""
if(la<lb):
    for i in range (0,lb-la):
        a="0"+a
    len=lb
if(la>lb):
    for i in range (0,la-lb):
        b="0"+b
for i in range (len-1,-1,-1):
    r1=int(a[i])+int(b[i])+jinwei
    if(r1==0):
        re=re+"0"
        jinwei=0
    elif(r1==1):
        re = re+"1"
        jinwei = 0
    elif(r1==2):
        re =re+"0"
        jinwei = 1
    else:
        re=re+"1"
        jinwei=1
if(jinwei==0):
    print(re[::-1])
else:
    print("1"+re[::-1])










