import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
A= [int(e) for e in digits ]
clock=[-1]*4
isvalid=1
for i in range(4):
    if A[i]<=2 and A[i]>clock[0]:
        clock[0]=A[i]
if clock[0]!=-1:
    del(A[A.index(clock[0])])
if clock[0]==2:
    for i in range(3):
        if A[i]<=3 and A[i]>clock[1]:
            clock[1]=A[i]
else:
    for i in range(3):
        if A[i]<=9 and A[i]>clock[1]:
            clock[1]=A[i]
if clock[1]!=-1:
    del(A[A.index(clock[1])])
for i in range(2):
    if A[i]<=5 and A[i]>clock[2]:
        clock[2]=A[i] 
if clock[2]!=-1:
    del(A[A.index(clock[2])])
clock[3]=A[0]
for i in range(4):
    if clock[i]==-1:
        isvalid=0
        break
if isvalid==0:
    print("")
else:
    hour=str(clock[0])+str(clock[1])
    minute=str(clock[2])+str(clock[3])
    print(hour+":"+minute)