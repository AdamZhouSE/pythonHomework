import heapq


def func(matrix, k):
    global num
    n = len(matrix)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    t = 0
    while t < k:
        num, row_index, col_index = heapq.heappop(heap)
        col_index += 1
        if col_index < n:
            heapq.heappush(heap, (matrix[row_index][col_index], row_index, col_index))
        t += 1
    return num


n =int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split(",")))
k =int(input())
res = func(matrix, k)
print(res)