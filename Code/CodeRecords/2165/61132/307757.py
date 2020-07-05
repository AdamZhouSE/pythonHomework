def hamon():
    que = [nodelist.index(source)]
    vis[nodelist.index(source)]=True
    ans.append(source)
    while len(que)>0:
        f = que.pop(0)
        tolist = edges[f]
        for i in range(len(tolist)):
            if (not vis[i]) and tolist[i]>0:
                vis[i]=True
                que.append(i)
                ans.append(nodelist[i])

ans = []
t = int(input())
nodelist = []
vis = []
edges=[]
for i in range(t):
    n,source = map(int,input().split())
    nodelist = input().split()
    vis = [False for x in range(n)]
    for j in range(int(n)):
        edges.append([int(x) for x in input().split()[1:]])    
    hamon()
    print(*ans)