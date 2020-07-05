# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:28:33 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    count=0
    for ev in num:
        count=count+abs(abs(ev)-1)
    if count==0 and num!=[1]:
        print(2)
    else:
        print(count)