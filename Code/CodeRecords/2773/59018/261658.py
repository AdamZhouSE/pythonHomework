import sys
def longestIncreasingPath(matrix):
        if not matrix or not matrix[0]: return 0

        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            # 方法一
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and \
                        matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            lookup[i][j] = max(res, lookup[i][j])
            

a=[]
lines=sys.stdin.readlines()[1:-1]
for i in range(len(lines)-1):
    a.append(eval(lines[i][2:-2]))
a.append(eval(lines[-1][2:-1]))  
print(longestIncreasingPath(a))
