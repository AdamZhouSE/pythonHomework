from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res

n=int(input())
matrix=[]
i=0
while i<n:
    s=input().split(",")
    #print(s)
    s=list(map(int,s))
    matrix.append(s)
    i=i+1
k=int(input())

j=Solution()
print(j.maxSumSubmatrix(matrix,k))

