import bisect
matrix = [list(map(int, input().split(','))) for _ in range(eval(input()))]
k = eval(input())
m, n = len(matrix), len(matrix[0])
preSum = [[0 for _ in range(n + 1)] for _ in range(m)]

for i in range(m):
    for j in range(1, n + 1):
        preSum[i][j] = preSum[i][j - 1] + matrix[i][j - 1]

res = float('-inf')
for colA in range(1, n + 1):
    for colB in range(colA, n + 1):
        s_list, cur = [0], 0
        for row in range(m):
            cur += preSum[row][colB] - preSum[row][colA - 1]
            idx = bisect.bisect_left(s_list, cur - k)
            if idx < len(s_list):
                res = max(res, cur - s_list[idx])
            bisect.insort(s_list, cur)
print(res)