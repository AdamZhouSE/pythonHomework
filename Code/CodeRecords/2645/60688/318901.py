piles=eval(input())
H=int(input())
K=sum(piles)//H-1
while(True):
    t=0
    for a in range(0,len(piles)):
        if(piles[a]%K!=0):
            t=t+piles[a]//K+1
        else:
            t=t+piles[a]//K
    if(t<=H):
        break
    K=K+1
print(K)