R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
length = []
matrix = []
for i in range(R):
    for j in range(C):
        temp = abs(r0 - i) + abs(c0 - j)
        length.append(temp)
        matrix.append([i, j])
for i in range(len(length)):
    for j in range(len(length) - 1):
        if length[j] > length[j + 1]:
            length[j], length[j + 1] = length[j + 1], length[j]
            matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
print(matrix)