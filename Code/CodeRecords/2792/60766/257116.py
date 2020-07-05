# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:55:30 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    
    res1=num.count(1)
    res2=''
    for i in range(len(num)-1):
        if num[i+1]==1:
            res2=res2+str(num[i])+' '
    res2=res2+str(num[-1])
    print(res1)
    print(res2)