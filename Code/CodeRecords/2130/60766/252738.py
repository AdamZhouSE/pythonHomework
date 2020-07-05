# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:09:47 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    num=''
    for i in range(1, n+1):    
        num=num+str(i)
    print(num[n-1])