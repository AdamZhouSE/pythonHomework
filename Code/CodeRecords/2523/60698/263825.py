# 22
matrix = list(eval(input()))
m = len(matrix)
n = len(matrix[0])
for i in range(0, m):
    diag = list()
    for j in range(0, n):
        if i + j >= m:
            break
        else:
            diag.append(matrix[i + j][j])
            diag.sort()
    for k in range(0,n):
        if i+k>=m:
            break
        else:
            matrix[i+k][k]=diag[k]
for i in range(0, n):
    diag = list()
    for j in range(0, m):
        if i + j >= n:
            break
        else:
            diag.append(matrix[j][j+i])
            diag.sort()
    for k in range(0, m):
        if i + k >= n:
            break
        else:
            matrix[k][k+i] = diag[k]
print(matrix)
