# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:14:14 2020

@author: Lenovo
"""

def printResult():
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    odd=[]
    qwe=[]
    for i in range(n):
        if num[i]%2==0:
            qwe.append(num[i])
        else:
            odd.append(num[i])
    odd=sorted(odd)[::-1]
    qwe=sorted(qwe)
    res=odd+qwe
    for i in res:
        print(i, end=' ')

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        printResult()
        print()