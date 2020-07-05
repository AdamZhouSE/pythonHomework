#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    temp=0
    len =int(input())
    l= [int(x) for x in input().split(" ")]
    left=[]
    right=[]
    for j in range (1,len-1):
        left = l[0:j]
        right = l[j + 1:]
        left.sort()
        right.sort()
        if (left[j - 1] <= l[j] and right[0] >=l[j]):
            print(l[j])
            temp = 1
            break

    if(temp==0):
        print(-1)