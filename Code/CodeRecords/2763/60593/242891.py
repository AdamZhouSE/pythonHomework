def dfs(pre,cur,cnt):
    global m,n,ans
    if(cur>m or cnt==n):
        return
    if(cur>=pre*2):
        cnt+=1
        if(cnt==n):
            ans+=1
        dfs(cur,cur+1,cnt)
        cnt-=1
    dfs(pre,cur+1,cnt)
t=int(input())
for tt in range(t):
    ans=0
    m,n=map(int,input().split())
    dfs(0,1,0)
    print(ans)