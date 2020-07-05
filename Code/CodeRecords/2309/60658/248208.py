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
        if f not in graph:
            return#表示没有源点或者汇点，匹配数为0，直接返回
        for to,weight,reverse in graph[f]:
            #如果流量大于0，且还未到过，更新level
            if weight>0 and level[to]<0:
                level[to]=level[f]+1
                que.append(to)

    

def dfs(s,t,f):
    """
    s,t,f:start,sink,flow
    """
    # print("start dfs from %d to %d with capaticy %d"%(s,t,f))
    if s==t:
        return f
    for i in graph[s]:
        #如果可以向下走
        if i[1]>0 and level[s]<level[i[0]]:
            d = dfs(i[0],t,min(f,i[1]))
            if d>0:
                i[1]-=d
                graph[i[0]][i[2]][1]=graph[i[0]][i[2]][1]+d
                # print("update graph[%d]"%s)
                # print(graph)
                return d
    return 0            

def dicnic(s,t):
    """
    source,sink
    """
    flow = 0
    # print("source %d sink %d"%(s,t))
    while True:
        bfs(s)
        # print("get level from bfs %s"%str(level))
        if(level[t]<0):
            return flow
        f = dfs(s,t,0x3f3f3f3f)
        while f>0:
            flow+=f
            # print("update flow %d"%flow)
            f = dfs(s,t,0x3f3f3f3f)
        



row,col = [int(x) for x in input().split()]
source = row*col+1
sink = row*col+2
level = []
graph ={}
previousline=[0 for x in range(col)]
ans = 0
for i in range(row):
    li = input()
    for j in range(col):
        if li[j]=='*':
            continue
        elif li[j]=='2':
            ans+=1
        elif li[j]=='1':
            add_edge(source,mark_node(i,j),1)
            if i>0 and previousline[j]=="3":
                add_edge(mark_node(i,j),mark_node(i-1,j),1)
            if j>0 and li[j-1]=="3":
                add_edge(mark_node(i,j),mark_node(i,j-1),1)
            if j<col-1 and li[j+1]=="3":
                add_edge(mark_node(i,j),mark_node(i,j+1),1)
        elif li[j]=="3":
            add_edge(mark_node(i,j),sink,1)
            if i>0 and previousline[j]=="1":
                add_edge(mark_node(i-1,j),mark_node(i,j),1)
    previousline = li
# print(graph)
ans+=dicnic(source,sink)
print(ans)