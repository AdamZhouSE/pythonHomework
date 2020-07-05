from typing import List
num=list(input().split(","))
for i in range(len(num)):
    num[i]=int(num[i])
num.sort()
n=len(num)
maxn=max(num[n - 1] - num[1] - n + 2,num[n - 2] - num[0] - n + 2)
minn=maxn
r=0
for i in range(len(num)):
    while r + 1 < n and num[r + 1] - num[i] + 1 <= n:
        r+=1
    last=n-r+i-1
    if r - i + 1 == n - 1 and num[r] - num[i] + 1 == n - 1:
        last = 2
    minn=min(minn,last)
res=[]
res.append(minn)
res.append(maxn)
print(res)