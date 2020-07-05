# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:42:52 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    count=0
    while n>1:
        if n%2==0:
            n=n/2
            count=count+1
        else:
            n=n-1
            count=count+1
    print(count)