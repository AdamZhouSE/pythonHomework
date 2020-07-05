# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:40:30 2020

@author: Lenovo
"""

if __name__ == '__main__':
    num=eval(input())
    low=int(input())
    upp=int(input())
    
    res=0
    for i in range(len(num)):
        for j in range(i+1, len(num)+1):
            su=0
            if j==i:
                su=num[j]
            else:
                su=sum(num[i:j])
            if su>=low and su<=upp:
                res=res+1
    print(res)