import re
n = int(input())
matrix = []
for i in range(0, n):
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    matrix.append(s)
m = int(input())
r, c = n, len(matrix[0])
pre = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + matrix[i-1][j-1]
res = l = 0
for i in range(r + 1):
    for j in range(c + 1):
        while i + l <= r and j + l <= c and pre[i + l][j + l] - pre[i + l][j] - pre[i][j + l] + pre[i][j] <= m:
            res = l
            l += 1
print(res)