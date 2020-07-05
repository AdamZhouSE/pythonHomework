import math
piles=eval(input())
H=int(input())
k=1
time=H+1
while time>H:
    time=0
    for i in range(len(piles)):
        time=time+math.ceil(piles[i]/k)
    k+=1
print(k-1)