# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:20:38 2020

@author: Lenovo
"""

if __name__ == '__main__':
    line=input().split(',')
    num=list(map(int, line))
    
    a=max(num)
    num.pop(num.index(a))
    b=max(num)
    num.pop(num.index(b))
    c=max(num)
    num.pop(num.index(c))
    
    print(a*b*c)
    