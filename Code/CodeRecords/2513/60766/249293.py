# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:07:15 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    num=[]
    for i in range(n):
        line=input().split(',')
        num.append(list(map(int, line)))
    k=int(input())
    nu=[]
    for i in range(n):
        nu=nu+num[i]
    nud=sorted(nu)
    print(nud[k-1])