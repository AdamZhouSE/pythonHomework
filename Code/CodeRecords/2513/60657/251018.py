import math
import  re
n=int(input())
cons=[]
for i in range(n):
    temp=input().split(',')
    temp=[int(x) for x in temp]
    for k in temp:
        cons.append(k)
want=int(input())
def find(A,B):
    A.sort()
    return A[B-1]
print(find(cons,want))