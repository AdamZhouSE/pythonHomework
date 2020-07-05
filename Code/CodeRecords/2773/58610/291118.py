s = ""
try:
    t = ""
    while t != ']':
        t = input()
        s = s + t
except Exception:
    pass
matrix = eval(s)
from functools import lru_cache
import itertools

r, c, d = len(matrix), len(matrix[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))

@lru_cache(None)
def f(i, j):
    t = 0
    for di, dj in d:
        x, y = i + di, j + dj
        if 0 <= x < r and 0 <= y < c and matrix[x][y] > matrix[i][j]:
            t = max(t, f(x, y))
    return t + 1

print(max(f(i, j) for i, j in itertools.product(range(r), range(c))))