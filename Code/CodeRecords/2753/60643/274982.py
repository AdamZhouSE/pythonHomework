import collections
import heapq#堆
def find_min_cost(n,flights,src,dst,K):
    graph = collections.defaultdict(dict)#生成一个字典，字典的value值也是字典
    for u, v, w in flights:
        graph[u][v] = w

    best = {}
    pq = [(0, 0, src)]#堆的初始值
    while pq:#堆不为空
        cost, k, place = heapq.heappop(pq)#k为中转航班次数
        if k > K + 1 or cost > best.get((k, place), float('inf')):
            continue
        if place == dst:
            return cost
        for nei, wt in graph[place].items():
            newcost = cost + wt
            if newcost < best.get((k + 1, nei), float('inf')):
                heapq.heappush(pq, (newcost, k + 1, nei))
                best[k + 1, nei] = newcost

    return -1


if __name__=="__main__":
    n=int(input())
    edges=eval(input())
    src=int(input())
    dst=int(input())
    k=int(input())
    res=find_min_cost(n,edges,src,dst,k)
    print(res)