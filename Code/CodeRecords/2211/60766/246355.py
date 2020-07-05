# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:42:55 2020

@author: Lenovo
"""

Asc=[]
Num=[]

def matching(k, que):
    global Asc, Num
    if k<0 and (len(que)>0 or que!=''):
        return False
    if len(que)>len(Asc):
        return False
    if que=='' or len(que)==0:
        return True
    if Asc[k]==que[0]:
        if matching(Num[k]-1, que[1:]):
            return True
    else:
        return False

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    for i in range(n):
        line=input().split()
        Asc.append(line[0])
        Num.append(int(line[1]))
    
    ques=''
    count=0
    for i in range(m):
        count=0
        que=input()
        ques=ques+que+' '
        for k in range(n):
            if matching(k, que):
                count=count+1
        print(count)   
        