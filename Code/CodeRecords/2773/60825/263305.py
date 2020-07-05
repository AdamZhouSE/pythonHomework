from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n, res = len(matrix), len(matrix[0]), 0
    cache = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            cur_len = dfs(i, j, matrix, cache, m, n)
            res = max(res, cur_len)
    return res


def dfs(i: int, j: int, matrix: List[List[int]],
        cache: List[List[int]], m: int, n: int) -> int:
    if cache[i][j] != -1:
        return cache[i][j]
    res = 1
    for x_offset, y_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = i + x_offset, j + y_offset
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
            continue
        length = 1 + dfs(x, y, matrix, cache, m, n)
        res = max(length, res)
    cache[i][j] = res
    return res


s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        ts=ts[2:]
        if ts[len(ts)-1]==',':
            ts=ts[:len(ts)-1]
        ts=ts[1:len(ts)-1]
        l=ts.split(",")
        ls=[]
        for x in l:
            ls.append(int(x))
        s.append(ls)
print(longest_increasing_path(s))