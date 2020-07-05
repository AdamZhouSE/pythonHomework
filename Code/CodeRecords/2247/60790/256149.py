piles=input().split(",")
piles=list(map(int,piles))
n=len(piles)
def dp(i,j):
    if(i>j):
        return 0
    player=(j-i-n)%2
    if(player==1):
        return max(piles[i]+dp(i+1,j),piles[j]+dp(i,j-1))
    else:
        return min(-piles[i]+dp(i+1,j),-piles[j]+dp(i,j-1))
print(dp(0,n-1)>0)
