import queue
def bfs(adj, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        ans.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)

ans=[];
Total=int(input());
i=0;
while(i<Total):
    s=input().split(" ");
    size=int(s[0]);
    start=s[1];
    nodeList=input().split(" ");
    j=0;
    graph={};
    while(j<size):
        s=input().split(" ");
        x=j+1;
        temp=[];
        while(x<len(s)):
            if(s[x]=='1'):
                temp.append(nodeList[x-1]);
            x+=1;
        graph[nodeList[j]]=temp;
        j+=1;
    bfs(graph, start);
    y=0;
    while(y<len(ans)-1):
        print(ans[y],end=" ");
        y+=1;
    print(ans[len(ans)-1]);
    i+=1;