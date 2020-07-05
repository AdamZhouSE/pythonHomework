# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:43:49 2020

@author: Lenovo
"""

if __name__ == '__main__':
    arr=eval(input())
    arr=sorted(arr)
    t=input()
    res=''
    for i in arr:
        if i > t:
            res=i
            break
    if res!='':
        print(res)
    else:
        print('c')