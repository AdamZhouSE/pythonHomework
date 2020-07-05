N,M=map(int,input().split())
grid=[]
for i in range(N):
    grid.append(list(input()))
ro=[[0 for i in range(M)] for j in range(N)]
co=[[0 for i in range(M)] for j in range(N)]
num=1
for i in range(N):
    for j in range(M):
        if grid[i][j]!='#':
            if j!=0:
                if grid[i][j-1]=='#':
                    num+=1
            ro[i][j]=num
    num+=1
nx=[i for i in range(1,max(map(max,ro))+1)]
num=1
for i in range(M):
    for j in range(N):
        if grid[j][i]!='#':
            if j!=0:
                if grid[j-1][i]=='#':
                    num+=1
            co[j][i]=num
    num+=1
ny=[i for i in range(1,max(map(max,co))+1)]
edge={x:{y:0 for y in ny} for x in nx}
for i in range(N):
    for j in range(M):
        if grid[i][j]=='*':
            edge[ro[i][j]][co[i][j]]=1
cx={x:-1 for x in nx}
cy={y:-1 for y in ny}
visited={y:0 for y in ny}
current_edge=[]
def max_match(nx,ny,cx,cy,visited,edge,current_edge):
    res=0
    for i in nx:
        res+=path(nx,ny,cx,cy,visited,edge,current_edge,i)#从当前行区域u搜索一个v与之匹配
    return res
def path(nx,ny,cx,cy,visited,edge,current_edge,u):
    flag=False#当前节点是否有连接
    for v in ny:#对所有列区域v
        if edge[u][v] and not visited[v]:#uv可连接且v没有被连接
            flag=True
            visited[v]=1
            cx[u] = v
            cy[v] = u
            current_edge.append((u, v))
            return 1  # 连接uv返回1
    if not flag:#如果在所有区域中都没有找到可连接的u
        for v in ny:#对列区域v
            if edge[u][v] and ((cy[v],v) in current_edge):#uv可连接且已经有uv对连接
                current_edge.remove((cy[v],v))#移除原先连接v的uv对,假设v已被当前u连接
                if path(nx,ny,cx,cy,visited,edge,current_edge,cy[v]):#如果原先的u能够找到新的v
                    cx[u]=v
                    cy[v]=u
                    current_edge.append((u,v))
                    return 1#连接uv返回1
                else:#否则恢复原先状态
                    current_edge.append((cy[v],v))
    return 0#所有情况均不允许时返回0
print(max_match(nx,ny,cx,cy,visited,edge,current_edge),end="")
