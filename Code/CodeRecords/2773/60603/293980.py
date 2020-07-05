import sys
import itertools
from functools import lru_cache
def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    r, c, d = len(matrix), len(matrix[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))
    @lru_cache(None)
    def f(i, j):
        t = 0
        for di, dj in d:
            x, y = i + di, j + dj
            if 0 <= x < r and 0 <= y < c and matrix[x][y] > matrix[i][j]:
                t = max(t, f(x, y))
        return t + 1
    return max(f(i, j) for i, j in itertools.product(range(r), range(c)))

a=[]
lines=sys.stdin.readlines()[1:-1]
for i in range(len(lines)-1):
    a.append(eval(lines[i][2:-2]))
a.append(eval(lines[-1][2:-1]))  
print(longestIncreasingPath(a))