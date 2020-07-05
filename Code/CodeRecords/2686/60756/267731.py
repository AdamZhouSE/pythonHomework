def dp(grid:list,K:int,n:int,p:int)->int:
    if n<len(grid):
        if K==0:
            return 0
        else:
            ans=0
            for i in range(p,len(grid[n])):
                if grid[n][i]>0:
                    ans=max(ans,dp(grid,K-1,i+1,i+1)+grid[n][i])
            return ans
    else:
        return 0


T=int(input())
for t in range(T):
    K=int(input())
    N=int(input())
    arr=list(map(int,input().split()))
    grid=[[0 for i in range(N)] for j in range(N-1)]
    for i in range(N-1):
        for j in range(i+1,N):
            grid[i][j]=arr[j]-arr[i]
    print(dp(grid,K,0,0))