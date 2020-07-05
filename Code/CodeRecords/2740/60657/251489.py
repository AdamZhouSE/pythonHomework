import math
import  re
A=input()
A=A[1:-1]
A=A.split(',')


def change(A):
    cons=[]
    for i in range(len(A)):
        hour=int(A[i][1:3])
        minute=int(A[i][4:6])
        now=hour*60+minute
        cons.append(now)
    cons.sort()
    want=[]
    for i in range(len(cons)-1):
        for k in range(i+1,len(cons)):
            if cons[k]>720 and cons[i]==0:
                want.append(1440-cons[k])
            else:
                want.append(cons[k]-cons[i])
    return min(want)
print(change(A))