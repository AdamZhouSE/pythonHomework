import numpy as np
import sys

nums1 = [x for x in input().strip()]
grid = [nums1]

while True:
    line1 = sys.stdin.readline().strip()
    if line1 == '':
        break
    tempNums = [x for x in line1]
    grid.append(tempNums)

column = len(nums1)
row = len(grid)
ufSet = np.full((row, column), -1)

# print(ufSet)
for j in range(1, column):
    if grid[0][j - 1] == '1' and grid[0][j] == '1':
        ufSet[0][j] = 1

for i in range(1, row):
    if grid[i - 1][0] == '1' and grid[i][0] == '1':
        ufSet[i][0] = 1

for i in range(1, row):
    for j in range(1, column):
        if grid[i][j - 1] == '1' and grid[i][j] == '1':
            ufSet[i][j] = 1
            if grid[i - 1][j] == '1' and grid[i][j] == '1':
                ufSet[i - 1][j] = 1
        if grid[i - 1][j] == '1' and grid[i][j] == '1':
            ufSet[i][j] = 1

res = 0
for i in range(0, row):
    for j in range(0, column):
        if grid[i][j] == '1' and ufSet[i][j] == -1:
            res += 1
print(res)