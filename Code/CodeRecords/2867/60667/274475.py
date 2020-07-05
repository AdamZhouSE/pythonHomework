import math
matrix = []

pace = 0
for i in range(5):
    matrix.append(list(map(int,input().split())))
for i in range(5):
    if 1 in matrix[i]:
        pace+=math.fabs(i-2)
        pace+=math.fabs(matrix[i].index(1)-2)
print(int(pace))