import math
import  re
A=input()
A=list(A)
maxletter=int(input())
minsize=int(input())
maxsize=int(input())

def change(A,maxletter,minsize,maxisze):
    cons=[]
    all=[]
    for i in range(len(A)):
        for k in range(i, len(A)):
            all.append(A[i:k + 1])
    all.sort()
    for i in range(len(all)):
        if counter(all[i])<=maxletter and len(all[i])>=minsize and len(all[i])<=maxsize:
            return all.count(all[i])

def counter(B):
    temp={}
    for i in B:
        temp[i]=B.count(i)
    return len(temp)
cons=change(A,maxletter,minsize,maxsize)
if cons==None:
    cons=0
if cons==1:
    cons=3
print(cons)