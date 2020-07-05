n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(1,len(l)-1):
    if(l[i]==0 and l[i-1]==l[i+1] and l[i-1]==1):
        l[i+1]=0
        ans+=1
print(ans)