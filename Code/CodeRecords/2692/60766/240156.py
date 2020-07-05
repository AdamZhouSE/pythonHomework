# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:23:12 2020

@author: Lenovo
"""

import copy

def delete(t, ox):
    #print('Delete : ')
    #print(t)
    #print(ox)
    while len(ox)>0 and t>=ox[0]:
        t=t-ox[0]
        ox.pop(0)
    return ox

def lawful(t, d, ox):
    #print(t)
    #print(d)
    #print(ox)
    for i in range(d):
        if len(ox)==0 or ox==[]:
            return True
        else:
            ox=delete(t, ox)
    if len(ox)==0 or ox==[]:
            return True
    return False

if __name__ == '__main__':
    ox=eval(input())
    t=copy.deepcopy(ox)
    d=int(input())
    
    temp=sum(ox)//d
    
    while not lawful(temp, d, ox):
        temp=temp+1
        ox=copy.deepcopy(t)
    print(temp)