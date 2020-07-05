piles=input().split(',')
piles=list(map(int,piles))
sum_a=0
sum_l=0
cnt=0
while len(piles)>0:
    if cnt%2==0:
        if piles[0]>=piles[len(piles)-1]:
            sum_a+=piles.pop(0)
        else:
            sum_a+=piles.pop()
    else:
        if piles[0]>=piles[len(piles)-1]:
            sum_l+=piles.pop(0)
        else:
            sum_l+=piles.pop()
    cnt+=1
print(True if sum_a>sum_l else False)