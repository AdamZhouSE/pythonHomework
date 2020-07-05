# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:06:41 2020

@author: Lenovo
"""

import copy

def adjust(num):
    i=0
    while i<(len(num)-1):
        if num[i][1]>=num[i+1][0]:
            num[i][1]=max(num[i][1], num[i+1][1])
            num.pop(i+1)
            i=i-1
        i=i+1

def lawful(num):
    for i in range(len(num)-1):
        if num[i][1]>=num[i+1][0]:
            return False
    return True

if __name__ == "__main__":
    num=eval(input())
    a=eval(input())
    num.append(a)
    num=sorted(num)
    t=copy.deepcopy(num)
    
    while not lawful(num):
        adjust(num)
    #if len(num)==4:
        #print(t)
    print(num)