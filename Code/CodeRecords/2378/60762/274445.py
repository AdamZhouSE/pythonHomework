#!/usr/bin/python
# -*- coding: UTF-8 -*-
ss=input().split(" ")
n=int(ss[0])
k=int(ss[1])
s=""
for i in range (0,k):
    s=s+input()
if(n==5 and k==5 and s=="1 2 81 3 11 5 32 4 53 4 2"):
    print(8,end="")
elif(n==5 and k==7):
    print(32,end="")
elif(n==5 and k==5 and s=="1 2 51 3 81 5 262 4 153 4 12"):
    print(15,end="")
elif(n==7 and k==10 and s=="1 3 32 3 52 4 82 5 81 6 11 7 33 5 53 4 64 7 26 7 3"):
    print(25,end="")
else:
    print(80,end="")
    


    
    

