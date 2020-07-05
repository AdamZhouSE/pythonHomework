# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:07:52 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    if len(num)<2:
        if num==[0]:
            print('UP')
        else:
            #print(num)
            print(-1)
    elif num[-1]>num[-2]:
        if num[-1]==15:
            print('DOWN')
        else:
            print('UP')
    else:
        if num[-1]==0:
            print('UP')
        else:
            print('DOWN')