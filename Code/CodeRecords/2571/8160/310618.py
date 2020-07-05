class Solution:
    def maxSumSubmatrix(self, matrix, k):
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res


import sys

lines = []
for line in sys.stdin:
    lines.append(line)
k = int(lines[len(lines)-1].replace("\n", ""))
data = []
for i in range(1, len(lines) - 1):
    temp1 = lines[i].replace("\n", "").split(",")
    data.append(temp1)
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
print(Solution().maxSumSubmatrix(data, k))