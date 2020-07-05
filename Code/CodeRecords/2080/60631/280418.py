import queue
 
def bfs(adj, start,names):
    out=[]
    visited = set()
    q = queue.Queue()
    visited.add(start)
    q.put(start) #把起始点放入队列
    while not q.empty():
        u = q.get_nowait()
        out.append(u)
        #print(u,end=' ')
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.put(v)
    return out

t=int(input())
for ti in range(t):
    s=input().split(' ')
    n=int(s[0])
    start=s[1]
    names=input().split(' ')
    graph={}
    for i in names:
        line=input()
        li=[]
        for j in range(4):
            if line[2:].split(' ')[j]=='1':
                li.append(names[j])
        graph[line[0]] = li
    
    out =  bfs(graph,start,names)
    
    for i in out:
        if out.index(i)==len(out)-1:
            print(i,end='')
        else:
            print(i,end=' ')
    print()
    
    
    