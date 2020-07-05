row=int(input())
column=int(input())
matrix=[]
for i in range(1,row+1):
    matrix.append([])
    for j in range(1,column+1):
        matrix[i-1].append(i*j)

from heapq import *
def kthSmallest( matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    minheap = []

    row = len(matrix)
    column=len(matrix[0])
    for i in range(min(k, row)):  # 当k小于n时，只需遍历前k行
        heappush(minheap, (matrix[i][0], i, 0))  # 堆里的每个元素是（matrix[i][j], i, j）

    counter = 0
    x, i, j = 0, 0, 0
    while counter < k:
        counter += 1
        x, i, j = heappop(minheap)
        if j < column - 1:
            heappush(minheap, (matrix[i][j + 1], i, j + 1))  # 向堆里加入该元素所在行的下一个元素
    return x
print(kthSmallest(matrix,int(input())))