from typing import List
def longest_increase_path(matrix: List[List[int]]) -> int:
    m, n, res = len(matrix), len(matrix[0]), 0
    # 用于记录每个点的最长递增路径的长度
    cache = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            # 每次寻找该点的最长递增路径的长度，并且更新全局的长度
            cur_len = dfs(i, j, matrix, cache, m, n)
            res = max(res, cur_len)
    return res


def dfs(i: int, j: int, matrix: List[List[int]], cache: List[List[int]], m: int, n: int) -> int:#i j为当前矩阵点的横纵坐标
    # 如果不等于-1，说明之前已经有记录了(即包含了这个点的最长递增路径的长度)
    res=1
    if cache[i][j] != -1:
        return cache[i][j]
    for x_offset, y_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:#上下左右四个方向的偏移量
        x= i + x_offset
        y= j + y_offset
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
            continue
        length = 1 + dfs(x, y, matrix, cache, m, n)
        res=length
    # 记录当前这个点的最长递增路径长度
    cache[i][j] = res#length是局部变量
    return res


if __name__ == '__main__':
    matrix = []  # 一行一行输入矩阵 需要处理输入部分
    line = input()
    while line != "]":
        temp = []
        for i in line:
            if i.isdecimal():
                temp.append(i)
        if len(temp) > 0:  # 去掉第一行line读入的"["的情况
            matrix.append(temp)
        line = input()
    print(longest_increase_path(matrix))