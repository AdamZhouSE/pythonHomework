# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:26:37 2020

@author: Lenovo
"""

def printResult():
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    evl=sorted(num)
    if num==evl[::-1]:
        print(0)
        return
    table=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if num[i]<num[j]:
                table[i][j]=1
    count=0
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j]==1:
                count=max(count, j-i)
    print(count)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        printResult()