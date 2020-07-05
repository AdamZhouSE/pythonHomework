# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:24:16 2020

@author: Lenovo
"""

if __name__ == '__main__':
    count=1
    line=input().split()
    n=int(line[0])
    c=int(line[1])
    line=input().split()
    num=list(map(int, line))
    
    for i in range(n-1):
        if num[i+1]-num[i]>c:
            count=1
        else:
            count=count+1
    if c==0:
        print(0)
    else:
        print(count)