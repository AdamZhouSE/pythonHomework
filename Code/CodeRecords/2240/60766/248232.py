# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:40:47 2020

@author: Lenovo
"""

def geta(num, i, j):
    l=num[:i]
    r=num[j:]
    n=l+r
    return sum(n)/len(n)

def canGeta(num, average):
    for i in range(0, len(num)-1):
        for j in range(i+1, len(num)):
            if geta(num, i, j)==(sum(num[i:j])/(j-i)):
                return True
    return False

if __name__ == '__main__':
    line=input().split(',')
    num=list(map(int, line))
    
    average=sum(num)/len(num)
    if average in num:
        print(True)
    else:
        print(canGeta(num, average))