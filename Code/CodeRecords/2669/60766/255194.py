# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:51:34 2020

@author: Lenovo
"""

def printson(n):
    res=''
    for i in range(n+1):
        if n&i==i:
            res=str(i)+' '+res
    print(res)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        num=int(input())
        printson(num)