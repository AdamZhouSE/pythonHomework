n=int(input())
profit=[]
res=0
for _ in range(n):
    p=int(input())
    profit.append(p)
    if len(profit)==1:
        res+=p
    else:
        profit.sort()
        idx=profit.index(p)
        diff1=profit[idx]-profit[idx-1] if idx>0 else float('inf')
        diff2=profit[idx+1]-profit[idx] if idx+1<len(profit) else float('inf')
        res+=min(diff1,diff2)
print(res,end='')
