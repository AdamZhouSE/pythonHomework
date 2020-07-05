n,m,q = [int(x) for x in input().split()]
edges = [0 for i in range(m+1)]
s = [(0,0,0,0,0) for i in range(q+1)]
dp = [[0x3f3f3f for i in range(n+1)] for j in range(n+1)]
pos = q
ans = [False for i in range(q+1)]
for i in range(1,m+1):
    edges[i]=[int(x) for x in input().split()]
for i in range(1,1+q):
    s[i]=tuple([int(x) for x in input().split()]+[i])
s.sort()
for i in range(m,0,-1):
    u,v = edges[i]
    dp[u][v]=dp[v][u]=i
    for j in range(1,n+1):
        dp[u][j] = min(dp[u][j],dp[v][j])
        dp[v][j] = min(dp[v][j],dp[u][j])
    while(s[pos][0]==i):
        ans[s[pos][-1]]=dp[s[pos][2]][s[pos][3]]<=s[pos][1]
        pos-=1
for i in range(1,1+q):
    print("Yes" if ans[i] else "No")