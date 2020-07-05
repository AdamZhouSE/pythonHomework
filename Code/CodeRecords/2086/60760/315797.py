def func(n:int,maps:list):
    graph = [[float("Inf") for x in range(n)] for y in range(n)]
    for i in maps:
        graph[i[0] - 1][i[1] - 1] = i[2]
    for i in range(n):
        graph[i][i] = 0     #邻接矩阵
    v=[]  #最小生成树的顶点
    father=[i for i in range(n)] #已有顶点的终点
    e=[] #放存进最小生成树的边
    res=0 #最小生成树代价
    edges=sorted(maps,key=lambda x:(x[2]))  #排序
    i=0#edges的索引
    while len(v)<n:
        if father[edges[i][0]-1]!=father[edges[i][1]-1]: #没有回路

            if v.count(edges[i][0])>0 and v.count(edges[i][1])>0:
                if father[edges[i][1]-1]!=father[edges[i][0]-1]:   #两个连通分量连通
                    temp=father[edges[i][0]-1]
                    for j in range(n):
                        if father[j]==temp:
                            father[j]=father[edges[i][1]-1]

            elif v.count(edges[i][1])>0:
                father[edges[i][0] - 1]=father[edges[i][1]-1]
            else :
                father[edges[i][1]-1]=father[edges[i][0]-1]
            if v.count(edges[i][0]) == 0:
                v.append(edges[i][0])
            if v.count(edges[i][1]) == 0:
                v.append(edges[i][1])
            e.append(edges[i])
            res+=edges[i][2]
        i+=1
    return res
first=list(map(int,input().split(' ')))
n=first[0]   #顶点数
m=first[1]   #边数
maps=[]
for i in range(m):  #第一个数是开始顶点，第二个数是结束顶点，第三位是路长
    maps.append(list(map(int,input().split(' '))))
print(func(n,maps),end="")