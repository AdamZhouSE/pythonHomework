#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
list=[]
list.append(0)
list.append(1)
index2=1
index3=1
index5=1
for i in range(2,n+1):
    list.append(min(list[index2]*2,list[index3]*3,list[index5]*5))
    if(list[i]==list[index2]*2):
        index2+=1
    if(list[i]==list[index3]*3):
        index3+=1
    if (list[i] == list[index5] * 5):
        index5+=1
print(list[n])
