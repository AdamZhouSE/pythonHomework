n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
d=[0 for i in range(len(arr))]
for i in range(len(arr)):
    if arr[i]<=k:
        ans+=1
        d[i]=1
    else:
        break
for i in range(len(arr)-1,-1,-1):
    if d[i]==1:
        break
    if arr[i]<=k:
        ans+=1
    else:
        break
print(ans)