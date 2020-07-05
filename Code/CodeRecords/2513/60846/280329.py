from heapq import *

def kthSmallest( matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    minheap = []
    n = len(matrix)
    for i in range(min(k, n)):  # 当k小于n时，只需遍历前k行
        heappush(minheap, (matrix[i][0], i, 0))  # 堆里的每个元素是（matrix[i][j], i, j）

    counter = 0
    x, i, j = 0, 0, 0
    while counter < k:
        counter += 1
        x, i, j = heappop(minheap)
        if j < n - 1:
            heappush(minheap, (matrix[i][j + 1], i, j + 1))  # 向堆里加入该元素所在行的下一个元素
    return x


rows=int(input())
nums=[]
for row in range(rows):
    nums.append(eval("["+input()+"]"))
print(kthSmallest(nums,int(input())))