# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:37:59 2020

@author: Lenovo
"""

if __name__ == '__main__':
    lin=input().split(',')
    lin[0]=lin[0][1:]
    lin[-1]=lin[-1][:-1]
    line=list(map(int, lin))
    
    a=sorted(line)
    print(a)