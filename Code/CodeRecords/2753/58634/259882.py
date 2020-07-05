# Dijkstra
import queue

def findCheapestPrice(flights, src, dst, K) -> int:
    graph = {} #初始化图
    for begin, end, cost in flights:
        if begin not in graph:
            graph[begin] = {end: cost}
        else:
            graph[begin][end] = cost
    q = queue.PriorityQueue()# 优先级队列
    q.put((0, src, K))# 用来保存其他顶点到已经经过的顶点的最短路径长度，没有路径就不填入，根据元组的第一个元素排序，每次取最小的那个长度
    while not q.empty():
        pre, begin, k = q.get() #之前的费用，这一站，K
        if begin == dst:
            return pre
        if k >= 0:
            for end in graph.get(begin, []):
                q.put((pre + graph[begin][end], end, k - 1))
    return -1

n = int(input())
edges = eval(input())
src = int(input())
dst = int(input())
k = int(input())
print(findCheapestPrice(edges,src,dst,k))



''' 有点问题 因为规定了长度k，
cost = 0
prices = [10000]*n
path = [0]*n，指向的是最短路径倒数第二个顶点
length = 0
graph = collections.defaultdict(dict)
for i in edges:
    x = i[0]
    y = i[1]
    price = i[2]
    graph[x][y] = price
    if x == 0:
        prices[y] = price #更新从0到这个点的距离


while length<=n: #遍历完了所有的K了
    newcost = min(prices)
    cost += newcost
    length += 1
    nextDst = prices.index(newcost)
    path[nextDst] =
    if newcost==dst:
        break
    if graph[nextDst]!={}:
        for i in graph[nextDst].keys():
            if graph[nextDst][i] + newcost < prices[i]:
                prices[i] = graph[nextDst][i] + newcost
'''



