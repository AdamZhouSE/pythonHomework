# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:36:28 2020

@author: Lenovo
"""

if __name__ == '__main__':
    num=eval(input())
    count=0
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if num[i]>2*num[j]:
                count=count+1
    print(count)