'''给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0'''


def sum(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = [[0 for i in range(col + 1)] for j in range(row + 1)]
    for i in range(1,row + 1):
        for j in range(1,col + 1):
            res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + matrix[i - 1][j - 1]
    return res


def solve():
    num = int(input())
    matrix = []
    for i in range(0,num):
        matrix.append(list(map(int,input().split(','))))
    threshold = int(input())
    p = sum(matrix)

    row = len(matrix)
    col = len(matrix[0])
    res = 2
    ans = 0
    for c in range(1,col + 1):
        for r in range(1,row + 1):
            edge_max = min(col + 1 - c,row + 1 - r)
            for i in range(res,edge_max + 1):
                s = p[r + i - 1][c + i - 1] - p[r - 1][c + i - 1] - p[r + i - 1][c - 1] + p[r - 1][c - 1]
                if s <= threshold:
                    ans = i
                    res = i
                else:
                    break

    return ans


print(solve())

