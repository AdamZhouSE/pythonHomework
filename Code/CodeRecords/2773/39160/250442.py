import sys, string
import numpy as np

try:
    mx = []
    while True:
        m = sys.stdin.readline().strip()
        if m == '' :
            break
        if m != '[' and m != ']':
            m = eval(m.strip(string.punctuation))
            mx.append(m)
    matrix = np.array(mx)
except:
    pass

row = len(matrix)
col = len(matrix[0])
lookup = [[0] * col for _ in range(row)]
    
def dfs(i, j):
    if lookup[i][j] != 0:
        return lookup[i][j] 
    val = matrix[i][j]
    lookup[i][j] = 1 + max(
        dfs(i + 1, j) if 0 <= i + 1 < row and 0 <= j < col and matrix[i + 1][j] > val else 0,
        dfs(i - 1, j) if 0 <= i - 1 < row and 0 <= j < col and matrix[i - 1][j] > val else 0,
        dfs(i, j + 1) if 0 <= i < row and 0 <= j + 1 < col and matrix[i][j + 1] > val else 0,
        dfs(i, j - 1) if 0 <= i < row and 0 <= j - 1 < col and matrix[i][j - 1] > val else 0,
    )
    return lookup[i][j]
    
print(max(dfs(i, j) for i in range(row) for j in range(col)))
 