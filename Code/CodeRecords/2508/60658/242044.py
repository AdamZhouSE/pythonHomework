def dfs(pre,cur):
    depth = 0
    for i in graph[cur]:
        #i=(to,weight)
        to,weight = i
        if to==pre:
            continue
        # print("start dfs from %d to %d"%(cur,to))
        depth+=dfs(cur,to)+1
        # print("end dfs from %d to %d depth %d"%(cur,to,depth))
        # print("weight = %d "%weight)
        for j in range(depth,0,-1):
            for k in range(j,0,-1):
                # print("update")
                # print("update dp[%d][%d]"%(cur,j))
                dp[cur][j]=max(dp[cur][j],dp[cur][j-k]+dp[to][k-1]+weight)
        # print(dp)
    return depth

ans = 0
n,q = [int(x) for x in input().split()]
graph = {}
dp=[]
for i in range(n+1):
    dp.append([0 for i in range(n+1)])

for i in range(n-1):
    fr,to,weight = [int(x) for x in input().split()]
    if fr in graph:
        graph[fr].append(tuple([to,weight]))
    else:
        graph[fr]=[tuple([to,weight])]
    if to in graph:
        graph[to].append(tuple([fr,weight]))
    else:
        graph[to]=[tuple([fr,weight])]
# print(graph)
dfs(0,1)
print(dp[1][q])