info=[int(x) for x in input().split()]
n,m=info[0],info[1]
graph=[[0]*(n+1) for i in range(n+1)]
alter=[]
def add_edge(u,v):
    graph[u][v]=graph[v][u]=1
    
for i in range(n-1):
    edge=[int(x) for x in input().split()]
    add_edge(edge[0],edge[1])
for i in range(m):
    info=[int(x) for x in input().split()]
    alter.append(info)
for i in range(1,n):
    cur=0
    if i==3:
        cur+=1
    elif i>3:
        cur+=2
    ans=alter[cur][2]
    print(ans)