# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:18:19 2020

@author: Lenovo
"""


def allFactor(n):
    if n <=3: return [0]
    tmp = n
    rlist = [1]
    i = 2
    while i <= tmp:
        if tmp % i == 0:
            rlist.append(i)
        i += 1
    return rlist if n != rlist[-1] else rlist[:-1]

if __name__ == '__main__':
    n=int(input())
    print(sum(allFactor(n))==n)