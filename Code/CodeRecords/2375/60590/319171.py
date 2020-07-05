def minSpanningTree(edge):
    lowcost = [0]*len(edge)
    nervex = [0]*len(edge)
    res = []  #这道题记录加进来的边的权值就好
    nervex[0] = -1  #先选中0号节点
    for i in range(1,len(edge)):  #初始化
        lowcost[i] = edge[0][i]
        nervex[i] = 0
    for i in range(1,len(edge)):  #加入n-1条边
        min = 1000000000
        v = 0
        for j in range(1,len(edge)):
            if(nervex[j]!=-1 and lowcost[j]<min):
                min = lowcost[j]
                v = j
        if(v!=0):
            res.append(lowcost[v])
            nervex[v] = -1
            #开始更新
            for x in range(1,len(edge)):
                if(nervex[x]!=-1 and edge[v][x]<lowcost[x]):
                    lowcost[x] = edge[v][x]
                    nervex[x] = v
    return res
temp = input().split()
n = int(temp[0])
k = int(temp[1])
edge = [[100000]*n for i in range(n)]
total = 0
test=[]
for x in range(k):
    temp = input().split()
    test.append(temp)
    edge[int(temp[0])-1][int(temp[1])-1] = min(int(temp[2]),edge[int(temp[0])-1][int(temp[1])-1])
    edge[int(temp[1])-1][int(temp[0])-1] = min(int(temp[2]),edge[int(temp[1])-1][int(temp[0])-1])
    total += int(temp[2])
res = minSpanningTree(edge)
print(max(res),end ="")