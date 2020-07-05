l1=eval('['+input().replace(' ',',')+']')
l2=eval('['+input().replace(' ',',')+']')
n=l1[0];k=l1[1]
ans=9999999
for i in l2:
    if k%i==0:
        ans=min(ans,k//i)
print(ans)