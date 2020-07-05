# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:56:14 2020

@author: Lenovo
"""

def cantra(a, b, c):
    return a+b>c and a+c>b and b+c>a

def checkif(num):
    for i in range(len(num)-2):
        for j in range(i+1, len(num)-1):
            for k in range(j+1, len(num)):
                if cantra(num[i], num[j], num[k]):
                    print('YES')
                    return
    print('NO')

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    num=sorted(num)
    
    checkif(num)