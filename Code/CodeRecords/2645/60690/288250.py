import math
piles=input()[1:-1].split(",")
for i in range(len(piles)):
    piles[i]=int(piles[i])
H=int(input())
sum=0
for e in piles: sum+=e
k=math.ceil(sum/H)

while 1:
    time=0
    for e in piles:
        time+=math.ceil(e/k)
    if time<=H:break
    else: k+=1
print(k)