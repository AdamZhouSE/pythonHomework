import queue
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
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
            if k >=0:
                for t in dic.get(f, []):
                    q.put((pre + dic[f][t], t, k-1))
        return -1

n=int(input());
flights=input();
src=int(input());
dst=int(input());
k=int(input());
flights=flights.replace("[","")
flights=flights.replace("]","")
print(flights)