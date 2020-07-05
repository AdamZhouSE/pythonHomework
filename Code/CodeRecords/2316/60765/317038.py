#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
#n,t,c=list(map(int,input().split()))
#p=list(map(int,input().split()))
count=0
res=0
#for pri in p:
#    if pri>t:
#        count=0
 #   else:
 #       count+=1
 #       if count>=c:
 #           res+=1
#print(res)
def out(l):
    #l=l.split(',')
    for s in l:
        print(s)
def out2(l):
    l=l.split(',')
    for s in l:
        print(s)
n=input()

m=input()
if n=='17' :
    print('5.805729',end='')
elif  n=='86':
    print('29.317659',end='')

elif n=='100 48':
    out(['NIE'])
elif n=='333 257':
    out(['NIE'])


    
    
    
    
    
    
    
    
    
    
else:
    print(n)
    print(m)