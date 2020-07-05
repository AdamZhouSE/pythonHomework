import queue
n=int(input())
q=queue.PriorityQueue()
arr=[int(x) for x in input().split()]
for num in arr:
    q.put(num)
total=0
while q.qsize()!=1:
    a=q.get()
    b=q.get()
    total+=a+b
    q.put(a+b)
print(total)
