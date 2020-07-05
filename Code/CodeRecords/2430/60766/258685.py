# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:32:12 2020

@author: Lenovo
"""

def printResult():
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    k=int(input())
    if sum(num)<k:
        print(-1)
        return
    res=[]
    i=0
    while i<len(num):
        #print('i : '+str(i))
        if k-num[i] in num:
            res.append(num[i])
            res.append(k-num[i])
            qw=num.pop(i)
            num.pop(num.index(k-qw))
            if len(num)<2:
                break
            #print(num)
            continue
        i=i+1
    
    if len(res)==0 or res==[]:
        print(-1)
    
    for i in range(len(res)//2):
        temp=''
        temp=temp+str(res[i*2])+' '+str(res[i*2+1])+' '+str(k)
        print(temp)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        printResult()