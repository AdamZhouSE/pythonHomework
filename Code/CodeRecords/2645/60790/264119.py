import math
s=input().strip("[")
s=s.strip("]")
piles=s.split(",")
piles=list(map(int,piles))
h=int(input())
def possible(k):
    count=0
    for i in piles:
        count+=math.ceil(i/k)
    return count<=h
left,right=1,max(piles)
while(right>left):
    mid=(right+left)//2
    if(possible(mid)):
        right=mid
    else:
        left=mid+1
print(right)
