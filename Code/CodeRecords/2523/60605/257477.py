matrix = list(eval(input().strip()))
rows = len(matrix)
cols = len(matrix[0])

## 先从rows开始处理
for i in range(rows - 1, -1, -1):
    # i 为当前开始行
    j = 0
    temp = []
    ii = i
    while 0 <= j < cols and ii < rows:
        temp.append(matrix[ii][j])
        ii += 1
        j += 1
    temp = sorted(temp)
    # print(temp)
    idx = 0
    j = 0
    ii = i
    while 0 <= j < cols and ii < rows:
        matrix[ii][j] = temp[idx]
        ii += 1
        j += 1
        idx += 1

# 再考虑col
for j in range(1, cols):
    # j为当前列
    i = 0
    temp = []
    jj = j
    while 0 <= jj < cols and i < rows:
        temp.append(matrix[i][jj])
        i += 1
        jj += 1
    temp = sorted(temp)
    idx = 0
    jj = j
    i = 0
    while 0 <= jj < cols and i < rows:
        matrix[i][jj] = temp[idx]
        i += 1
        jj += 1
        idx += 1
print(matrix)
