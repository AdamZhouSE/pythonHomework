#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
row=list(map(int,input().split()))
odd=[];add=0
for num in row:
    if num%2==0:
        add+=num
    else:
        odd.append(num)
odd.sort(reverse=True)
if len(odd)%2!=0:
    odd.pop()
for num in odd:
    add+=num
print(add)