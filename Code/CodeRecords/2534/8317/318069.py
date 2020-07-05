import heapq
arrays = input()
        
heap = []
for row, arr in enumerate(arrays):
    if arr: # maybe the arr is empty list
        heapq.heappush(heap, (arr[0], row, 0)) # push the tuple (element, row, col)
        
res = []
while heap:
    val, row, col = heapq.heappop(heap)
    res.append(val)
        
    col += 1
    if col < len(arrays[row]):
        heapq.heappush(heap, (arrays[row][col], row, col))

print(res)