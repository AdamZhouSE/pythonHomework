def dp(i,tar):
    if tar==0:
        return 0
    if tar==1:
        return cost[i]
    if i>=39:
        return float('inf')
    t,r=divmod(tar,x)
    return min(r*cost[i]+dp(i+1,t),(x-r)*cost[i]+dp(i+1,t+1))
x=int(input())
target=int(input())
cost=list(range(40))
cost[0]=2
print(dp(0,target)-1)
