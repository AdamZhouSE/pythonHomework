import queue
tests=int(input())
ans=[]
for t in range(tests):
    q=queue.Queue()
    graph={'':[]}
    req=input().split()
    n=int(req[0])
    root=req[1]
    src=input().split()
    for i in range(n):
        tmp=input().split()
        key=tmp[0]
        value=[int(x) for x in tmp[1:]]
        graph[key]=value
    q.put(root)
    while q.qsize()>0:
        tmp=q.get()
        if tmp not in ans:
            ans.append(tmp)
        for i in range(n):
            if graph[tmp][i]==1 and src[i] not in ans:
                q.put(src[i])
print(*ans)