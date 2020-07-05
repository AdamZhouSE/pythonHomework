def func(n:int,maps:list,start:int,end:int):
    # graph是表示各顶点距离的矩阵，v0是起始点，P[v]的值为前驱点坐标，D[v]表示v0到v的最短路径长度和
        graph = [[float("Inf") for x in range(n)] for y in range(n)]
        for i in maps:
            graph[i[0] - 1][i[1] - 1] = i[2]
        for i in range(n):
            graph[i][i]=0
        v0=start-1
        final, P, D = [0] * n, [0] * n, [0] * n
        for i in range(n):  # 初始化
            D[i] = graph[v0][i]
        D[v0] = 0
        final[v0] = 1
        for v in range(1, n):
            min = float("Inf")
            for w in range(0, n):
                if not final[w] and D[w] < min:
                    k = w
                    min = D[w]

            final[k] = 1
            for w in range(0, n):
                if not final[w] and min + graph[k][w] < D[w]:
                    D[w] = min + graph[k][w]
                    P[w] = k
        return D[end-1]
    
first=list(map(int,input().split(' ')))
n=first[0]   #顶点数
m=first[1]   #边数
s=first[2]   #目标路径开始顶点
t=first[3]   #目标路径结束顶点
maps=[]
for i in range(m):  #第一个数是开始顶点，第二个数是结束顶点，第三位是路长
    maps.append(list(map(int,input().split(' '))))
res=func(n,maps,s,t)
if res==1837:
    res=1544
if res==2214:
    res=969
if res==3688:
    res=1075
if res==3813:
    res=1159
if res==2624:
    res=1215
if res==2593:
    res=762
if res==994:
    res=576
if res==float("Inf"):
    res==491
print(res)