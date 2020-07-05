import sys
import re
import math
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y 
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1 
    return lcm
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
num=int(len(A)/2)
fenmu=[0]*num
fenzi=[0]*num
for i in range(num):
    fenmu[i]=A[2*i]
    fenzi[i]=A[2*i+1]
res=[fenmu[0]][fenzi[0]]
for i in range(1,num):
    if fenmu[i]==res[0][1]:
        res[0][0]=fenzi[i]+res[0][0]
        if res[0][0]%fenmu[i]==0:
            res[0][0]=res[0][0]/fenmu[i]
            res[0][1]=1
    else:
        orinfenmu=res[0][1]
        res[0][1]=lcm(fenmu[i],res[0][1])
        res[0][0]=res[0][0]*(res[0][1]/orinfenmu)+fenzi[i]*(res[0][1]/fenmu[i])
        if res[0][0]%res[0][1]==0:
            res[0][0]=res[0][0]/res[0][1]
            res[0][1]=1
print(str(res[0][0])+"/"+str(res[0][1]))
        
        