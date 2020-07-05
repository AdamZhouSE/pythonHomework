from heapq import heappop, heappush

points = eval(input())
K = int(input())
queue = []
distance = lambda x: points[x][0] ** 2 + points[x][1] ** 2
length = len(points)
for i in range(length):
    heappush(queue, (distance(i), points[i]))
res = []
for i in range(K):
    res.append((heappop(queue))[1])
print(res)
