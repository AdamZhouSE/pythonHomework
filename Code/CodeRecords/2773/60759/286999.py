from math import sqrt
from collections import defaultdict

ch = input()
matrix = defaultdict(list)
line = input()
x = 0
while line != ']':
    line = eval(line.rstrip(','))
    for y in range(len(line)):
        matrix[(x, y)] = [line[y], 1]
    line = input()
    x += 1
s_matrix = list(map(list, sorted(matrix.items(), key=lambda i: i[1][0])))
n = int(sqrt(len(matrix)))
ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for item in s_matrix[1:]:
    max_p = 0
    for d in ds:
        if 0 <= item[0][0] + d[0] < n and 0 <= item[0][1] + d[1] < n and \
                item[1][0] > matrix[(item[0][0] + d[0], item[0][1] + d[1])][0]:
            max_p = max(max_p, matrix[(item[0][0] + d[0], item[0][1] + d[1])][1])
    matrix[(item[0][0], item[0][1])][1] = 1 + max_p
print(max(matrix.values(), key=lambda i: i[1])[1])
