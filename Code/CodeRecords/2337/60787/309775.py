def mark_node(x,y):
    """
    把(x, y)标记为x*m+y，即线性数组的索引,x,y从0开始
    """
    return x*col+y

def add_edge(f,t,w):
    """
    ：param ：from,to,weight
    :return:
    """
    if f not in graph:
        graph[f] = []
    if t not in graph:
        graph[t] = []
    graph[f].append([t,w,len(graph[t])])
    graph[t].append([f,0,len(graph[f])-1])

def bfs(s):
    """
    :param s : source
    """
    global level
    level = [-1 for x in range(sink+1)]
    level[s]=0
    que = [s]
    while len(que)>0:
        f = que.pop(0)
        for to,weight,reverse in graph[f]:
            if weight>0 and level[to]<0:
                level[to]=level[f]+1
                que.append(to)
    return level

def dfs(s,t,f):
    """
    s,t,f:start,sink,flow
    """
    if s==t:
        return f
    for i in graph[s]:
        #如果可以向下走
        if i[1]>0 and level[s]<level[i[0]]:
            d = dfs(i[0],t,min(f,i[1]))
            if d>0:
                i[1]-=d
                graph[i[0]][i[2]][1]=graph[i[0]][i[2]][1]+d
                return d
    return 0

def dinic(s,t):
    """
    source,sink
    """
    flow = 0
    while True:
        bfs(s)
        if(level[t]<0):
            return flow
        f = dfs(s,t,0x3f3f3f3f)
        while f>0:
            flow+=f
            f = dfs(s,t,0x3f3f3f3f)

row,col = [int(x) for x in input().split()]
so = [list(input()) for x in range(row)]
temprow = -1
tempcol = -1
rowNO=[0 for x in range(col*row)]
colNO=[0 for x in range(col*row)]
for i in range(row):
    for j in range(col):
        if so[i][j]=="#":
            continue
        if j==0 or so[i][j-1]=="#":
            temprow+=1
        rowNO[mark_node(i,j)]=temprow
for j in range(col):
    for i in range(row):
        if so[i][j]=="#":
            continue
        if i==0 or so[i-1][j]=="#":
            tempcol+=1
        colNO[mark_node(i,j)]=tempcol
source = tempcol*temprow+1
sink = tempcol*temprow+2
level = []
graph ={}
for i in range(temprow+1):
    add_edge(source,i,1)
for i in range(tempcol+1):
    add_edge(1+i+temprow,sink,1)

for i in range(row):
    for j in range(col):
        if so[i][j]=="*":
            add_edge(rowNO[mark_node(i,j)],1+temprow+colNO[mark_node(i,j)],1)

ans = 0
ans+=dinic(source,sink)
print(ans,end="")