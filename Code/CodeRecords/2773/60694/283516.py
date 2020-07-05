d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(matrix: [[]], i: int, j: int):
    ans = 0
    for ele in d:
        x, y = i + ele[0], j + ele[1]
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
            ans = max(ans, dfs(matrix, x, y))
    ans += 1
    return ans


input()
matrix = []
x = input()
while x != "]":
    x = x.strip().strip(',')
    matrix.append(eval(x))
    x = input()

res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        res = max(res, dfs(matrix, i, j))
print(res)
