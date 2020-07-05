import heapq
arr=eval(input())
k=eval(input())
n=len(arr)
fra=[]
heap=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        fra.append([arr[i],arr[j]])
heap = [[float('-Inf'),1] for i in range(len(fra)-k+1)]
for i in fra:
    if -(i[0]/i[1]) > (heap[0][0]/heap[0][1]):
        heapq.heappop(heap)
        heapq.heappush(heap, [-i[0],i[1]])
print([-heap[0][0],heap[0][1]])