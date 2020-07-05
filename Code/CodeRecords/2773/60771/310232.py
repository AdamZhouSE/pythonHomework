#17
# M x N的矩阵
def dfs(i, j, matrix,cache, m, n):
    # 如果不等于-1，说明之前已经有记录了(即包含了这个点的最长递增路径的长度)
    if cache[i][j] != -1:
        return cache[i][j]
    res = 1
    for x_offset, y_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = i + x_offset, j + y_offset
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
            continue
        length = 1 + dfs(x, y, matrix, cache, m, n)
        res = max(length, res)
    # 记录当前这个点的最长递增路径长度
    cache[i][j] = res
    return res

matrix = []
c = input()

s = input()
while s != ']':
    if s.endswith(","):
        matrix.append(eval(s[:-1]))
    else:
        matrix.append(eval(s))
    s = input()
# c = input()
# print(matrix)
m = len(matrix)
n = len(matrix[0])
res = 0
#记录长度的缓存数组
# cache = [[-1]*n]*m
# print(cache)
cache = [[-1 for _ in range(n)] for _ in range(m)]
# print(cache)
for i in range(0,m):
    for j in range(0,n):
        cur_len = dfs(i,j,matrix,cache,m,n)
        res = max(res,cur_len)

print(res)