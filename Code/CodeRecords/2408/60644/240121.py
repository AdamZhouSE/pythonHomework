n=int(input())
s=0
res=True
ans=1
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            res=False
            break
    if res:
        s=s+1
    res=True
k=n-s
while s!=0:
    ans=ans*s
    s=s-1
while k!=0:
    ans=ans*k
    k=k-1
ans=ans%1000000000+7
print(ans)