from _testcapi import INT_MAX


def dijkstra(graph, startIndex, path, cost, max):
    """
        求解各节点最短路径，获取path，和cost数组，
         path[i] 表示vi节点的前继节点索引，一直追溯到起点。
         cost[i] 表示vi节点的花费
         """
    lenth = len(graph)
    v = [0] * lenth
    # 初始化 path，cost，V
    for i in range(lenth):
        if i == startIndex:
            v[startIndex] = 1
        else:
            cost[i] = graph[startIndex][i]
            path[i] = (startIndex if (cost[i] < max) else -1)
        # print v, cost, path
    for i in range(1, lenth):
        minCost = max
        curNode = -1
        for w in range(lenth):
            if v[w] == 0 and cost[w] < minCost:
                minCost = cost[w]
                curNode = w
        # for 获取最小权值的节点
        # if curNode == -1: break
        # 剩下都是不可通行的节点，跳出循环
        v[curNode] = 1
        for w in range(lenth):
            if v[w] == 0 and (graph[curNode][w] + cost[curNode] < cost[w]):
                cost[w] = graph[curNode][w] + cost[curNode] # 更新权值
                path[w] = curNode # 更新路径
        # for 更新其他节点的权值（距离）和路径
    return cost


num_list=list(map(int,input().split(' ')))
n=num_list[0]
m=num_list[1]
start=num_list[2]-1
dest=num_list[3]-1
max=INT_MAX
graph=[[max for i in range(n)] for j in range(n)]
for i in range(m):
    num_list = list(map(int, input().split(' ')))
    graph[num_list[0]-1][num_list[1]-1]=min(num_list[2],graph[num_list[0]-1][num_list[1]-1])
    graph[num_list[1] - 1][num_list[0] - 1] = min(num_list[2], graph[num_list[1] - 1][num_list[0] - 1])
path=[0]*n
cost=[0]*n
print(dijkstra(graph,start,path,cost,max)[dest])