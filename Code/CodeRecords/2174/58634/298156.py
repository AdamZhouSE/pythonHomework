def dijkstra(graph, startIndex, max):
    '''
    求解各节点最短路径，获取path，和cost数组，
    path[i] 表示vi节点的前继节点索引，一直追溯到起点。
    cost[i] 表示vi节点的花费
    '''
    lenth = len(graph)
    visited = [0] * lenth
    cost = [0]*lenth
    path = [0]*lenth
    # 初始化 path，cost，V
    for i in range(lenth):
        if i == startIndex:
            visited[startIndex] = 1
            path[i] = -2

        else:
            cost[i] = graph[startIndex][i]
            path[i] = (startIndex if (cost[i] < max) else -1)
    # print v, cost, path
    for i in range(1, lenth):
        minCost = max
        curNode = -1
        for w in range(lenth):
            if visited[w] == 0 and cost[w] < minCost:
                minCost = cost[w]
                curNode = w
    # for 获取最小权值的节点
        if curNode == -1: break
    # 剩下都是不可通行的节点，跳出循环
        visited[curNode] = 1
        for w in range(lenth):
            if visited[w] == 0 and (graph[curNode][w] + cost[curNode] < cost[w]):
                cost[w] = graph[curNode][w] + cost[curNode] # 更新权值
                path[w] = curNode # 更新路径
        # for 更新其他节点的权值（距离）和路径
    return path


graph = {}
n, q = map(int, input().split(" "))
risks = [([1000] * n) for i in range(n)]
for _ in range(q):
    affair = [int(i) for i in input().split(" ")]
    if affair[0] == 0:
        x, y, v = affair[1], affair[2], affair[3]
        if x not in graph.keys():
            graph[x] = []
            graph[x].append(y)
        else:
            if y not in graph[x]:
                graph[x].append(y)
        if y not in graph.keys():
            graph[y] = []
            graph[y].append(x)
        else:
            if x not in graph[y]:
                graph[y].append(x)
        risks[x][y] = v
        risks[y][x] = v
    elif affair[0] == 2:
        x,y = affair[1],affair[2]
        temp = risks.copy()
        all_path = dijkstra(temp,x,1000)
        if all_path[y] == -1:
            print(-1)
        else:
            path = []
            i = all_path[y] #回溯得到路线
            max_risk = risks[i][y]
            #print(max_risk, "First")
            while True:
                pre = i
                i = all_path[i]
                if i == x:
                    max_risk = max(max_risk, risks[pre][x])
                    break
                max_risk = max(max_risk, risks[pre][i])
            print(max_risk)
    else:
        x, y = affair[1], affair[2]
        graph[x].remove(y)
        if graph[x] == []:
            graph.pop(x)
        graph[y].remove(x)
        if graph[y] == []:
            graph.pop(y)
        risks[x][y] = 1000
        risks[y][x] = 1000


