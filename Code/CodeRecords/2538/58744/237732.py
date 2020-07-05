import queue

arr = eval(input())
min_heap = queue.PriorityQueue()

for num in arr:
    min_heap.put(num)

pre = 0
while not min_heap.empty:
    cur = min_heap.get()
    if cur - 1 > 0 and cur != pre + 1:
        print(pre + 1)
        break
    pre = cur