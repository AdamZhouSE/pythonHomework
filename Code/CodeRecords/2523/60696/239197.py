matrix = [i.split(',') for i in input()[2:-2].split('],[')]
for i in range(len(matrix)):
    matrix[i] = [int(j) for j in matrix[i]]

m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        temp = []
        if i-1 >= 0 and j-1 >= 0:
            continue
        while i < m and j < n:
            temp.append(matrix[i][j])
            i += 1
            j += 1
        temp.sort()
        for k in range(len(temp)):
            i -= 1
            j -= 1
            matrix[i][j] = temp[len(temp) - k - 1]

print(matrix)