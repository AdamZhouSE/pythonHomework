def find_min(arr, x, y):
    curr_dis = 1 << 31 - 1
    min_dis = 1 << 31 - 1
    for ii in range(len(arr)):
        for jj in range(len(arr[0])):
            if arr[ii][jj] == 0:
                curr_dis = abs(x-ii) + abs(y-jj)
                if curr_dis < min_dis:
                    min_dis = curr_dis
    return min_dis


matrix = []
try:
    while True:
        matrix.append([int(x) for x in input().split(" ")])
except EOFError:
    res = [[1 << 31-1]*len(matrix[0]) for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                res[i][j] = 0
            else:
                res[i][j] = find_min(matrix, i, j)
    for i in range(len(res)):
        for j in range(len(res[0])-1):
            print(res[i][j], end=" ")
        print(res[i][len(res[0])-1])
