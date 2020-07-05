# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:37:32 2020

@author: Lenovo
"""

if __name__ == '__main__':
    u=0
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    c=int(line[2])
    line=input().split()
    w=list(map(int, line))
    
    for i in range(n-m+1):
        if max(w[i:i+m])-min(w[i:i+m])<=c:
            u=1
            print(i+1)
    if u==0:
        print('NONE', end='')