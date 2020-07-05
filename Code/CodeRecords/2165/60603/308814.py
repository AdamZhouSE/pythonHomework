
def bfs():
    que = [nodelist.index(source)]
    visited[nodelist.index(source)]=True
    ans.append(source)
    while len(que)>0:
        f = que.pop(0)
        tolist = edges[f]
        for i in range(len(tolist)):
            if (not visited[i]) and tolist[i]>0:
                visited[i]=True
                que.append(i)
                ans.append(nodelist[i])
                
                

ans = []
t = int(input())
nodelist = []
visited = []
edges=[]
for i in range(t):
    n,source = input().split()
    nodelist = input().split()
    visited = [False for x in range(int(n))]
    for j in range(int(n)):
        edges.append([int(x) for x in input().split()[1:]])    
    # print(nodelist)
    # print(visited)
    # print(edges)
    bfs()
    print(*ans)