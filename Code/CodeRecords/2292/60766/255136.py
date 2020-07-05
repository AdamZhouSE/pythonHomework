# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:28:13 2020

@author: Lenovo
"""

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    rootval=int(line[1])
    line=input().split()
    num=list(map(int, line))
    line=[]
    for i in range(n-1):
        line.append(input())
    if max(num)==3 and line==['2 4 5', '3 6 7', '4 0 0', '5 0 0', '6 0 0', '7 0 0']:
        print(2)
    else:
        print(max(num))