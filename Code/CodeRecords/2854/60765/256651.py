#!/usr/bin/env python 
# -*- coding:utf-8 -*-

list1=list(map(int,input().split()))
num=set(list1)
flag=False
if len(num)>3 :
    print('Alien')
elif len(num)==1:
    print('Elephant')
else:
    count=list(map(list1.count,num))
    if 4 in count:
        if len(num)==2:
            print('Elephant')
        else:
            print('Bear')
    else:
        print('Alien')