#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
sum=0
posi=0
neg=0
zero=0
for i in range(n):
    if a[i]>0:
        posi+=1
        sum+=a[i]-1
    elif a[i]<0:
        neg+=1
        sum+=(-1-a[i])
    else:
        zero+=1
        sum+=1
if neg%2==1 and zero==0:
    sum+=2
print(sum)


        