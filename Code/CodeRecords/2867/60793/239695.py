import math
matrix = []
for i in range(0, 5):
    matrix.append(list(map(int, input().split(" "))))
tar = []
for i in range(0, 5):
    line = matrix[i]
    for j in range(0,5):
        if line[j] == 1:
            tar.append(i)
            tar.append(j)
result = abs(2 - tar[0]) + abs(2 - tar[1])
print(result)