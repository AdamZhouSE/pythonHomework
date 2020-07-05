ans = 0
n,q = [int(x) for x in input().split()]
graph = {}
dp = []


def dfs(pre,cur):
    depth = 0
    for i in graph[cur]:
        to,weight = i
        if to==pre:
            continue
        depth+=dfs(cur,to)+1
        for j in range(depth,0,-1):
            for k in range(j,0,-1):
                dp[cur][j] = max(dp[cur][j],dp[cur][j-k]+dp[to][k-1]+weight)
    return depth



for i in range(n+1):
    dp.append([0 for i in range(n+1)])

for i in range(n-1):
    fr,to,weight = [int(x) for x in input().split()]
    if fr in graph:
        graph[fr].append(tuple([to,weight]))
    else:
        graph[fr] = [tuple([to,weight])]
    if to in graph:
        graph[to].append(tuple([fr, weight]))
    else:
        graph[to] = [tuple([fr, weight])]

dfs(0,1)
print(dp[1][q])
