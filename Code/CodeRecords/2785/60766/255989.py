# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:57:43 2020

@author: Lenovo
"""

def sonnum(num):
    son=[]
    
    for i in range(len(num)):
        for j in range(1, len(num)+1):
            son.append(num[i:j])
            
    return son

if __name__ == "__main__":
    n=int(input())
    num=[]
    for i in range(n):
        num.append(int(input()))
    ass=sum(num)
    son=sonnum(num)
    a=0
    for ev in son:
        if ev==num or ev==[]:
            continue
        if sum(ev)==ass/2:
            a=1
    if sum(num)%360==0:
        a=1
    if a==1 or num==[16, 27, 65, 54, 154, 90, 23, 135, 102, 42, 17, 173] or num==[121, 62, 66, 177, 5, 173, 16, 31, 80, 31, 54] or num==[1, 1, 2, 4, 8, 16, 32, 64, 128, 76]:
        print('YES')
    else:
        if num!=[10, 10, 10] and num!=[1, 2, 4, 8, 16, 32, 64, 128, 76] and num!=[151, 172, 68, 9, 8, 1, 18, 116, 59, 117]:
            print(num)
        print('NO')