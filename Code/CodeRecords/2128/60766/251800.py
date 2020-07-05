# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:18:07 2020

@author: Lenovo
"""

if __name__ == '__main__':
    line=input().split(',')
    num=list(map(int, line))
    maxn=0
    for j in range(len(num)):
        count=0
        a=num[0]
        num=num[1:]
        num.append(a)
        for i in range(len(num)):
            count=count+i*num[i]
        maxn=max(maxn, count)
    print(maxn)