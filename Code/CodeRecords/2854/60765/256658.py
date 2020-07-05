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

    count=[list1.count(i) for i in num]
    if 4 in count:
        if len(num)==2:
            print('Elephant')
        else:
            print('Bear')
    elif 5 in count:
        print('Bear')
    else:
        print('Alien')