import heapq
t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    k=eval(input())
    heap=[float('-Inf') for i in range(k)]
    for i in arr:
        if -i>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,-i)
    print(-heap[0])