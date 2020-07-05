import collections
import itertools
matrix = eval(input())
m, n, d = len(matrix), len(matrix[0]), collections.defaultdict(list)
for i, j in itertools.product(range(m), range(n)):
    d[i-j].append(matrix[i][j])
d = {k: iter(sorted(v)) for k, v in d.items()}
for i, j in itertools.product(range(m), range(n)):
    matrix[i][j] = next(d[i-j])
print(matrix)



