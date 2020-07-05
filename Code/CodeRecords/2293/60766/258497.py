# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:02:49 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        le=int(input())
        line=input().split()
        num=list(map(int, line))
        k=int(input())
        num=sorted(num)
        print(num[k-1])