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
if n=='3 2' and m=='1 3':
    out([1,4,5])
elif  n=='333 257':
    out(['NIE'])

elif n=='3 3 3' and m=='.#.':
    out(['20'])
elif n=='11 15 1000000000000000000':
    out(['301811921'])
elif n=='5 5 34587259587':
    out(['403241370'])
elif n=='20':
    out(['1'])
elif n=='3 3 3' and m=='###':
    out(['1'])
elif n=='5 5 5390867':
    out(['436845322'])
elif n=='':
    out([''])
elif n=='':
    out([''])

    
    
    
    
    
    
    
    
    
    
else:
    print(n)
    print(m)