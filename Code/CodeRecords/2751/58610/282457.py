matrix = []
try:
    while True:
        matrix.append(list(map(int, input().split(' '))))
except Exception:
    pass
row, col = len(matrix), len(matrix[0])
for i in range(row):
    for j in range(col):
        if matrix[i][j] != 0:
            p = matrix[i - 1][j] if i else float('inf')
            q = matrix[i][j - 1] if j else float('inf')
            matrix[i][j] = min(p, q) + 1

for i in range(row - 1, -1, -1):
    for j in range(col - 1, -1, -1):
        p = matrix[i + 1][j] if i < row - 1 else float('inf')
        q = matrix[i][j + 1] if j < col - 1 else float('inf')
        matrix[i][j] = min(matrix[i][j], min(p, q) + 1)
for rows in matrix:
    print(*rows)
