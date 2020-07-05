import itertools
from decimal import *
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    b.append([int(x) for x in input().split()])
init=[x for x in range(n)]
all=[]
temp=itertools.permutations(init)
for i in temp:
    all.append(list(i))
maximum=0
for i in all:
    tempA=[]
    tempB=[]
    for j in range(n):
        tempA.append(a[j][i[j]])
        tempB.append(b[j][i[j]])
    maximum=max(maximum,sum(tempA)/sum(tempB))
print("%.6f" %maximum)