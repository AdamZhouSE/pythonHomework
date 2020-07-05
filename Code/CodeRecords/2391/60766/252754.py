# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:31:20 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    dic=[]
    for i in range(n):
        dic.append(input())
    m=int(input())
    dig=[]
    for i in range(m):
        t=input()
        if not t in dic:
            print('WRONG')
            continue
        if t in dig:
            print('REPEAT')
            continue
        print('OK')
        dig.append(t)