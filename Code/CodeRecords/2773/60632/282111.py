def dfs(i: int, j: int, row: int, col: int):
    if dp[i][j] > 0:
        return dp[i][j]
    maxi = 1
    for p in path:
        x = i + p[0]
        y = j + p[1]
        if 0 <= x < row and 0 <= y < col and matrix[x][y] > matrix[i][j]:
            len = 1 + dfs(x, y, row, col)
            maxi = max(maxi, len)
    dp[i][j] = maxi
    return maxi


matrix = []
while True:
    s = input().strip().strip(',')
    if s == ']':
        break
    elif s != '[':
        matrix.append(eval(s))
dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
path = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 下，上，右，左
# print(matrix)
ans = 0
row, col = len(matrix), len(matrix[0])
for i in range(row):
    for j in range(col):
        ans = max(ans, dfs(i, j, row, col))
print(ans)
