#!/usr/bin/python
# -*- coding: UTF-8 -*-
#[[0,0],[2,0],[1,1],[2,1],[2,2]]
import math
s=input().replace("[","").replace("]","")
la=math.ceil((len(s)+1)/8)
#地板取整
lista=[[]for i in range(la)]
for i in range(0,la):
    lista[i].append(int(s[i*8]))
    lista[i].append(int(s[i*8+2]))
lb=math.floor((len(s)+1)/8)
listb=[[]for i in range(lb)]
for i in range(0,lb):
    listb[i].append(int(s[4+i*8]))
    listb[i].append(int(s[4+i*8+2]))
lista=sorted(lista,key=(lambda x:[x[0],x[1]]),reverse=False)
listb=sorted(listb,key=(lambda x:[x[0],x[1]]),reverse=False)
#key= and False
#*args 代表可接受列表或者元祖作为参数， **args 代表可以接受字典作为函数的参数传入
numa=0
for i in range(0,la):
    if(lista.count([0,0])==1 and lista.count([0,1])==1 and lista.count([0,2])==1):
        numa=1
        break
    if (lista.count([1, 0]) == 1 and lista.count([1, 1]) == 1 and lista.count([1, 2]) == 1):
        numa = 1
        break
    if (lista.count([2, 0]) == 1 and lista.count([2, 1]) == 1 and lista.count([2, 2]) == 1):
        numa = 1
        break
    if (lista.count([0, 0]) == 1 and lista.count([1, 0]) == 1 and lista.count([2, 0]) == 1):
        numa = 1
        break
    if (lista.count([0, 1]) == 1 and lista.count([1, 1]) == 1 and lista.count([2, 1]) == 1):
        numa = 1
        break
    if (lista.count([0, 2]) == 1 and lista.count([1, 2]) == 1 and lista.count([2, 2]) == 1):
        numa = 1
        break
    if (lista.count([0, 0]) == 1 and lista.count([1, 1]) == 1 and lista.count([2, 2]) == 1):
        numa = 1
        break
    if (lista.count([0, 2]) == 1 and lista.count([1, 1]) == 1 and lista.count([2, 0]) == 1):
        numa = 1
        break
numb=0
for i in range(0,lb):
    if(listb.count([0,0])==1 and listb.count([0,1])==1 and listb.count([0,2])==1):
        numb=1
        break
    if (listb.count([1, 0]) == 1 and listb.count([1, 1]) == 1 and listb.count([1, 2]) == 1):
        numb = 1
        break
    if (listb.count([2, 0]) == 1 and listb.count([2, 1]) == 1 and listb.count([2, 2]) == 1):
        numb = 1
        break
    if (listb.count([0, 0]) == 1 and listb.count([1, 0]) == 1 and listb.count([2, 0]) == 1):
        numb = 1
        break
    if (listb.count([0, 1]) == 1 and listb.count([1, 1]) == 1 and listb.count([2, 1]) == 1):
        numb = 1
        break
    if (listb.count([0, 2]) == 1 and listb.count([1, 2]) == 1 and listb.count([2, 2]) == 1):
        numb = 1
        break
    if (listb.count([0, 0]) == 1 and listb.count([1, 1]) == 1 and listb.count([2, 2]) == 1):
        numb = 1
        break
    if (listb.count([0, 2]) == 1 and listb.count([1, 1]) == 1 and listb.count([2, 0]) == 1):
        numb = 1
        break
if(numa==1):
    print("A")
if(numb==1):
    print("B")
if(numa==0 and numb==0 and la+lb==9):
    print("Draw")
if(numa==0 and numb==0 and la+lb!=9):
    print("Pending")




















