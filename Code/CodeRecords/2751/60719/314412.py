def get(matrix):
    row = len(matrix)
    column = len(matrix[0])
    temp = matrix
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                temp[i][j] = 0
            else:
                temp[i][j] = 1000000000000
    for i in range(row):
        for j in range(column):
            if j > 0:
                temp[i][j] = min(temp[i][j-1]+1, temp[i][j])
            if i > 0:
                temp[i][j] = min(temp[i-1][j]+1, temp[i][j])
    for i in range(row):
        for j in range(column):
            if j > 0:
                temp[i][column-j-1] = min(temp[i][column-j]+1, temp[i][column-j-1])
            if i > 0:
                temp[row-i-1][j] = min(temp[row-1][j]+1, temp[row-i-1][j])
    return temp



import sys
matrix = []
line = sys.stdin.readline().strip()
while True:
    if line == "":
        break
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)
    line = sys.stdin.readline().strip()
res = get(matrix)
for i in range(len(res)):
    s = ""
    for j in range(len(res[0])):
        s += str(res[i][j])
        if j < len(res[0])-1:
            s += " "
    print(s)