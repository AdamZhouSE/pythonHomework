# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:52:58 2020

@author: Lenovo
"""

if __name__ == '__main__':
    line=input().split(',')
    num=list(map(int, line))
    if num[0]<=num[-1]:
        print(num[0])
    else:
        for i in range(len(num)-1):
            if num[i]>num[i+1]:
                print(num[i+1])
                break
            elif num[len(num)-1-i]<num[len(num)-2-i]:
                print(num[len(num)-1-i])
                break