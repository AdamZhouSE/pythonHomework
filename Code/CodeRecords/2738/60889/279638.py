rawMatrix = []
line = input()
while True:
    line = input()
    if line == "]":
        break
    else:
        line = list(map(int,line.strip("[\", ]").split("\",\"")))
        rawMatrix.append(line)
matrix = []
for i in rawMatrix:
    line = []
    count = 0
    for j in i:
        if j == 1:
            count = count + 1
        else:
            count = 0
        line.append(count)
    matrix.append(line)
maxSquare = 0
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        minLength = matrix[j][i]
        for k in range(j,len(matrix)):
            if matrix[k][i] < minLength:
                minLength = matrix[k][i]
            square = minLength * (k-j+1)
            if square>maxSquare:
                maxSquare = square
print(maxSquare)