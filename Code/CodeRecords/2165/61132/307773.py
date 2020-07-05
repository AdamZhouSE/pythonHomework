def bfs():
    que = [node.index(source)]
    vis[node.index(source)]=True
    ans.append(source)
    while len(que)>0:
        f = que.pop(0)
        tolist = edges[f]
        for i in range(len(tolist)):
            if (not vis[i]) and tolist[i]>0:
                vis[i]=True
                que.append(i)
                ans.append(node[i])

ans = []
t = int(input())
node = []
vis = []
edges=[]
for i in range(t):
    n,source = input().split()
    node = input().split()
    vis = [False for x in range(int(n))]
    for j in range(int(n)):
        edges.append([int(x) for x in input().split()[1:]])    
    bfs()
    print(*ans)