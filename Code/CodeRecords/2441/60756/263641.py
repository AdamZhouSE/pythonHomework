import heapq
arr=list(map(int,input()[1:-1].split(",")))
heapq.heapify(arr)
print([heapq.heappop(arr) for i in range(len(arr))])