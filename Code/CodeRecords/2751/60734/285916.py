matrix = []
try:
    for line in iter(input, sys.):
        matrix.append(list(map(int,line.split(' '))))
except:
    pass

base = 0
for time in range(len(matrix)*len(matrix[0])):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= base:
                count += 1
                continue
            hasfound = False
            # 上
            if (i > 0 and matrix[i-1][j] == base)\
                    or (i+1 < len(matrix) and matrix[i+1][j] == base)\
                    or (j > 0 and matrix[i][j-1] == base) \
                    or (j+1 < len(matrix[0]) and matrix[i][j+1] == base):
                hasfound = True
            if not hasfound:
                matrix[i][j] += 1
            else:
                count += 1
    if count == len(matrix[0])*len(matrix):
        break
    base += 1

#print
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j != len(matrix[0])-1:
            print(matrix[i][j], end=' ')
        else:
            print(matrix[i][j])