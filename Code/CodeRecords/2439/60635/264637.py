n=int(input())
node=[[]for i in range(n+1)]
graph=[[0 for k in range(n+1)] for j in range(n+1)]
def link(x,y,val):
    graph[x][y]=val
    node[x].append(y)
def findpath(start,end):
    tmp=node[start][0]
    if tmp==end:
        return graph[start][tmp]
    return graph[start][tmp] ^ findpath(tmp,end)
for i in range(n-1):
    info=input().split()
    x=int(info[0])
    y=int(info[1])
    val=int(info[2])
    link(x,y,val)
m=int(input())
for i in range(m):
    info = input().split()
    x = int(info[0])
    y = int(info[1])
    if x==y:
        print(graph[x][x])
    else:
        print(findpath(x,y))