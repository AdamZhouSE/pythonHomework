n=int(input())
a=list(map(int,input().split()))
sav=0
ans=0
beg=a[0]
for i in a:
    if(i>beg*2):
        ans=max(ans,sav)
        sav=0
    beg=i
    sav+=1
    ans=max(ans,sav)
print(ans)