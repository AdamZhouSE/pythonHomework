mat = eval(input())
for i in range(0, len(mat[0])):
    m, n = [0, i]
    temp = []
    while m < len(mat) and n < len(mat[0]):
        temp.append(mat[m][n])
        m += 1
        n += 1
    temp.sort()
    m, n, j = [0, i, 0]
    while m < len(mat) and n < len(mat[0]):
        mat[m][n] = temp[j]
        m += 1
        n += 1
        j += 1
for i in range(0, len(mat)):
    m, n = [i, 0]
    temp = []
    while m < len(mat) and n < len(mat[0]):
        temp.append(mat[m][n])
        m += 1
        n += 1
    temp.sort()
    m, n, j = [i, 0, 0]
    while m < len(mat) and n < len(mat[0]):
        mat[m][n] = temp[j]
        m += 1
        n += 1
        j += 1
print(mat)
