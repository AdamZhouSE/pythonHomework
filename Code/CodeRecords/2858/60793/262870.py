
length = int(input())
matrix = [[1 for i in range(0, length)]]
for i in range(1, length):
    matrix.append([1])
for i in range(1, length):
    row = matrix[i]
    for j in range(1, length):
        row.append(row[j - 1] + matrix[i - 1][j])
print(matrix[-1][-1])