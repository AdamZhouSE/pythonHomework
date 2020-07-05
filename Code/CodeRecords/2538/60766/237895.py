# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:05:36 2020

@author: Lenovo
"""

if __name__ == '__main__':
    line=input().split(',')
    line[0]=line[0][1:]
    line[-1]=line[-1][:-1]
    num=list(map(int, line))
    
    num=sorted(num)
    for i in range(1, max(num)+2):
        if i in num:
            continue
        else:
            print(i)
            break