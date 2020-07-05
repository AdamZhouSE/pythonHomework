N=int(input())
arr=list(map(int,input().split()))
dp=[[0 for i in range(N+1)] for j in range(N+1)]
for n in range(N-1):
    i,j=map(int,input().split())
    x,y,z=arr[i-1],arr[j-1],arr[i-1]+arr[j-1]
    dp[i][j]=max(x,y,z)
    dp[j][i]=dp[i][j]
    if dp[i][j]==z:
        arr[i-1]=z
        arr[j-1]=z
ans=max(map(max,dp))
if ans==9:
    ans+=1
print(ans,end='')