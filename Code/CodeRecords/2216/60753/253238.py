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
    fenzi[i]=A[2*i]
    fenmu[i]=A[2*i+1]
resfenzi=fenzi[0]
resfenmu=fenmu[0]
for i in range(1,num):
    if fenmu[i]==resfenmu:
        resfenzi=fenzi[i]+resfenzi
        if resfenzi%fenmu[i]==0:
            resfenzi=resfenzi/fenmu[i]
            resfenmu=1
    else:
        orinfenmu=resfenmu
        resfenmu=lcm(fenmu[i],resfenmu)
        resfenzi=resfenzi*(resfenmu/orinfenmu)+fenzi[i]*(resfenmu/fenmu[i])
        if resfenzi%resfenmu==0:
            resfenzi=resfenzi/resfenmu
            resfenmu=1
print(str(resfenzi)+"/"+str(resfenmu))
        
        