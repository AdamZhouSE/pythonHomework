import math
def minSpanningTree(edge,s):
    lowcost = [0]*len(edge)
    nervex = [0]*len(edge)
    res = []  #这道题记录加进来的边的权值就好
    nervex[0] = -1  #先选中0号节点
    for i in range(1,len(edge)):  #初始化
        lowcost[i] = edge[0][i]
        nervex[i] = 0
    for i in range(1,len(edge)):  #加入n-s条边
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
s = int(temp[0])
p = int(temp[1])
cordinate = [[0]*2 for i in range(p)]
for i in range(p):
    temp = input().split()
    cordinate[i][0] = int(temp[0])
    cordinate[i][1] = int(temp[1])
edge = [[10000]*p for i in range(p)]
for i in range(p):
    for j in range(p):
        temp = math.sqrt((cordinate[i][0]-cordinate[j][0])**2 + (cordinate[i][1]-cordinate[j][1])**2)
        edge[i][j] = temp
res = minSpanningTree(edge,s)
res.sort()
print("{:.2f}".format(res[p-s-1]),end = "")