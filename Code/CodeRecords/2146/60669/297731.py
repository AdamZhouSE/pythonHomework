def dijkstra():
    if k<=1:
        return -1
    else:
        dist=[[None]*(n-1) for z in range(n)]   # n行n-1列
        path=[[None]*(n-1) for z in range(n)]
        isDone=[]    # 记录已经定下来的点

        dijkstraFrom=fromWhere    # Dijkstra是一个特定节点到其他节点 所以初始化节点应该是fromwhere 课件上那个图是从0开始的
        for toCurrent in range(n):   # 初始化第一列
            if wayTime[dijkstraFrom][toCurrent]!=None:
                dist[toCurrent][dijkstraFrom]=wayTime[dijkstraFrom][toCurrent]
                path[toCurrent][dijkstraFrom]=0
        isDone.append(dijkstraFrom)

        count=0
        while count<n-2:   # 共n-1列 count从0开始 而且后面用的count和count+1
            fromCurrent=min(dist[x][count] for x in range(n) and (x not in isDone) and dist[x][count]!=None)
            for toCurrent in range(n) and toCurrent not in isDone:
                dist[toCurrent][count+1]=dist[toCurrent][count]  # 先变成和上一次一样的 如果可以变 下面会再改
                if toCurrent!=fromCurrent and wayTime[fromCurrent][toCurrent]!=None:
                    if dist[toCurrent][count]==None or (dist[fromCurrent][count]+wayTime[fromCurrent][toCurrent])<dist[toCurrent][count]:
                        dist[toCurrent][count+1]=dist[fromCurrent][count]+wayTime[fromCurrent][toCurrent]
                        path[toCurrent][count+1]=fromCurrent
            count+=1

        # 然后正常就直接dist[toWhere][n-2]就行了 但这个题还要根据path算可乐汉堡的问题 如果不行还要回看n-3,n-4...
        index=n-2
        while index>=0:
            sum=0
            pathArr=[toWhere]
            isOK=True
            while pathArr[0]!=fromWhere:
                pathArr.insert(0,path[pathArr[0]][index])
            for saleNum in pathArr:
                if sale[saleNum]==1:
                    sum+=1
                else:
                    sum-=1
                if abs(sum)>k:
                    isOK=False
                    break
            if isOK:
                return dist[toWhere][index]
            index-=1
        return -1




if __name__ == '__main__':
    time=eval(input())
    for w in range(time):
        tempArr=input().split(" ")
        n=eval(tempArr[0])
        m=eval(tempArr[1])
        k=eval(tempArr[2])
        sale=list(map(int,input().split(" ")))
        wayTime=[[None]*n for z in range(n)]
        for z in range(m):
            tempArr=list(map(int,input().split(" ")))
            wayTime[tempArr[0]-1][tempArr[1]-1]=tempArr[2]    # 输入给的是1 2,这里应该用0 1
        tempArr=input().split(" ")
        fromWhere=eval(tempArr[0])-1    # 同样减1，方便访问数组
        toWhere=eval(tempArr[1])-1
        print(dijkstra())