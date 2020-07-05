# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:58:27 2020

@author: Lenovo
"""

def printResult():
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    
    count=-1
    for i in range(n-1):
        for j in range(i+1, n):
            count=max(count, num[j]-num[i])
    print(count)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        printResult()