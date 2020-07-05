# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:56:03 2020

@author: Lenovo
"""

def High(num, h):
    count=0
    for i in num:
        if i>=h:
            count=count+1
    if count>=h:
        return True
    return False

if __name__ == '__main__':
    num=eval(input())
    h=max(num)
    while h>0:
        if High(num, h):
            break
        h=h-1
    print(h)