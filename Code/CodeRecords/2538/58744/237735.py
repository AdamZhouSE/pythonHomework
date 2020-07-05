import queue

arr = eval(input())
min_heap = queue.PriorityQueue()

for num in arr:
    min_heap.put(num)

pre = 0
while not min_heap.empty():
    cur = min_heap.get()
    if cur - 1 > 0 and cur != pre + 1:
        print(pre + 1)
        break
    elif min_heap.empty() and cur == pre + 1:
        if cur + 1 > 0:
            print(cur + 1)
        else:
            print(1)
    
    pre = cur
