# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:34:39 2020

@author: Lenovo
"""

def getmax(a, b):
    count=0
    i=a
    while i>0 and a-i<b:
        count=count+i
        i=i-1
    return count

def getmin(v):
    count=0
    for i in range(1, v+1):
        count=count+i
    return count

def getResult(num):
    a=num[0]
    b=num[1]
    if getmin(b)<=a and getmax(a, b)>=a:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        line=input().split()
        num=list(map(int, line))
        getResult(num)