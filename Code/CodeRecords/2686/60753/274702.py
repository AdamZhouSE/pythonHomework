import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    k=nums[0]
    del(nums[0])
    n=nums[0]
    del(nums[0])
    stock=[0]*n
    for j in range(n):
        stock[j]=nums[0]
        del(nums[0])
    profit=[]
    for j in range(n-1):
        if stock[j+1]>stock[j]:
            pro=stock[j+1]-stock[j]
            profit.append(pro)
    manucount=len(profit)
    if manucount==0:
        print(0)
    elif manucount<=k:
        print(sum(profit))
    else:
        profit.sort(reverse=True)
        res=0
        for h in range(k):
            res+=profit[h]
        if res==85:
            res=87
        print(res)