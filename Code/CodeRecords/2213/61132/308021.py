n,m,q = [int(x) for x in input().split()]
edges = [0 for i in range(m+1)]
s = [(0,0,0,0,0) for i in range(q+1)]
dp = [[0x222222 for i in range(n+1)] for j in range(n+1)]
posi = q
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
    while(s[posi][0]==i):
        ans[s[posi][-1]]=dp[s[posi][2]][s[posi][3]]<=s[posi][1]
        posi-=1
for i in range(1,1+q):
    print("Yes" if ans[i] else "No")