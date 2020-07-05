def diagonalSort(matrix):
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        temp = []
        k = min(row-i,column)
        for j in range(k):
            temp.append(matrix[i+j][j])
        temp.sort()
        for j in range(k):
            matrix[i+j][j] = temp[j]
    for i in range(column):
        temp = []
        k = min(column-i,row)
        for j in range(k):
            temp.append(matrix[j][i+j])
        temp.sort()
        for j in range(k):
            matrix[j][i+j] = temp[j]
    return matrix

matrix = eval(input())
print(diagonalSort(matrix))