import math
arrayString=input()
piles=eval(arrayString)
H=int(input())
n=len(piles)
sum=0
for j in range(n):
    sum+=piles[j]
h=sum//n
K=h
t=0
for i in range(n):
    t+=math.ceil(piles[i]/K)
if t<=H:
    print(K)
else:
    K+=1
    
    
    