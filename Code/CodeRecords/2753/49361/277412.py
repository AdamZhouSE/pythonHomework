import collections
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        heap = [(0, src, K + 1)]
        for s, d, c in flights:
            graph[s][d] = c
        while heap:
            cost, s, k = heapq.heappop(heap)
            if s == dst: return cost
            if k > 0:
                for d in graph[s]:
                    heapq.heappush(heap, (cost + graph[s][d], d, k - 1))
        return -1


n = int(input())
inputStr = input()
temp1 = inputStr.replace("[", "").replace("]", "").split(",")
src = int(input())
dst = int(input())
K = int(input())
group = int(len(temp1) / 3)
mylist = [[0] * 3 for _ in range(group)]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        mylist[i][j] = int(temp1[i * 3 + j])
print(Solution().findCheapestPrice(n, mylist, src, dst, K))