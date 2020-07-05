n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(i):
        if(abs(arr[i]-arr[j])<=k):
            ans+=1
print(ans*2)