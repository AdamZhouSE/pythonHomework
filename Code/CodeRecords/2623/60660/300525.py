import heapq
n=eval('['+input()+']')
k=int(input())
print(heapq.nlargest(k, n)[-1])