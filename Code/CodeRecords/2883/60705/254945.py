import math

line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
matrix = []
for i in range(0, n):
    matrix.append(list(input()))

count = 0
for i in range(0, n):
    for j in range(0, m):
        if matrix[i][j] == 'B':
            count += 1

radius = int((int(math.sqrt(count)) - 1)/2)
if radius == 0:
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 'B':
                print(i+1, end=" ")
                print(j+1)
else:
    for i in range(0, n):
        for j in range(0, m):
            found = True
            for k in range(0, radius+1):
                if matrix[i][k+j] != 'B' or matrix[i][k-1] != 'B' or matrix[i+k][j] != 'B' or matrix[i-k][j] != 'B':
                    found = False
            if found:
                print(i+1, end=" ")
                print(j+1)
