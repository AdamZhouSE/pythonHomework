#07
import sys
from builtins import str


def dfs(i, j):
    lands[i][j] = "0"
    for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        tmp_i = i + x
        tmp_j = j + y
        if 0 <= tmp_i < row and 0 <= tmp_j < col and lands[tmp_i][tmp_j] == "1":
            dfs(tmp_i, tmp_j)

lands = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    f = str(line).split(" ")
    for item in f:
        lands.append(list(item))

row = len(lands)
col = len(lands[0])
# print(row,col)
# print(lands)

cnt = 0
for i in range(row):
    for j in range(col):
        if lands[i][j] == "1":
            dfs(i, j)
            cnt += 1

print(cnt)