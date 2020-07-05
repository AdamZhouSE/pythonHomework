import queue
def findCheapestPrice(n: int, flights, src: int, dst: int, K: int) -> int:
    dic = {}
    for f, t, cost in flights:
        if f not in dic:
            dic[f] = {t: cost}
        else:
            dic[f][t] = cost
    q = queue.PriorityQueue()
    q.put((0, src, K))
    while not q.empty():
        pre, f, k = q.get()
        if f == dst: return pre
        if k >= 0:
            for t in dic.get(f, []):
                q.put((pre + dic[f][t], t, k - 1))
    return -1
n=int(input())
edges=eval(input())
src=int(input())
dst=int(input())
k=int(input())
print(findCheapestPrice(n,edges,src,dst,k))