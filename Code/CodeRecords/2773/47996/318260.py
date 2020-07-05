from functools import lru_cache
import itertools
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
str = input()
str = input()
temp = []
while str != "]":
    i = -1
    if str.endswith(","):
        i = -2
    str = str[3:i].split(",")
    str = [int(x) for x in str]
    temp.append(str)
    str = input()
print(longestIncreasingPath(temp))
