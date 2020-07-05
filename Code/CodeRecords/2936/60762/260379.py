#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
l=[]
for i in range (0,n):
    s=list(input().replace("-",""))
    for j in range (0,7):
        if(s[j]=="A" or s[j]=="B" or s[j]=="C"):
            s[j]="2"
        if(s[j]=="D" or s[j]=="E" or s[j]=="F"):
            s[j]="3"
        if(s[j]=="G" or s[j]=="H" or s[j]=="I"):
            s[j]="4"
        if (s[j] == "J" or s[j] == "K" or s[j] == "L"):
            s[j] = "5"
        if (s[j] == "M" or s[j] == "N" or s[j] == "O"):
            s[j] = "6"
        if (s[j] == "P" or s[j] == "R" or s[j] == "S"):
            s[j] = "7"
        if (s[j] == "T" or s[j] == "U" or s[j] == "V"):
            s[j] = "8"
        if (s[j] == "W" or s[j] == "X" or s[j] == "Y"):
            s[j] = "9"

    l.append("".join(s))
ll=list(set(l))
temp=0
for i in ll:
    if(l.count(i)>1):
        temp=1
        print(i[0:3]+"-"+i[3:]+" "+str(l.count(i)))
if(temp==0):
    print("No duplicates.",end="")














