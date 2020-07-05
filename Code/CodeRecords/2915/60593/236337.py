n=int(input())
a=list(map(int,input().split()))
sav=1
ans=0
beg=a[0]
for i in range(1,n):
    if(a[i]>beg*2):
        ans=max(ans,sav)
        beg=a[i]
        sav=0
    sav+=1
ans=max(ans,sav)
print(ans)