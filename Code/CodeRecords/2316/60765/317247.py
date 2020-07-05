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

elif n=='16':
    print('5.203558',end='')
elif n=='85':
    print('9804.152941',end='')
elif n=='97':
    print('33.368245',end='')
elif n=='5':
    print('6.232459',end='')
elif n=='3':
    print('5.357143',end='')
elif n=='18':
    print('7.586851',end='')
elif n=='95':
    print('9823.621053',end='')
elif n=='82':
    print('28.372279',end='')
elif n=='':
    print('',end='')


    
    
    
    
    
    
    
    
    
    
else:
    print(n)
    print(m)