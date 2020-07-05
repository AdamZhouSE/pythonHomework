def sum_square(matrix, start_line, start_column, length):
    result = 0
    for i in range(start_line, start_line+length):
        for j in range(start_column, start_column+length):
            result += matrix[i][j]
    return result


mat = []
line = int(input())
for i in range(0, line):
    mat.append([int(x) for x in input().split(',')])
threshold = int(input())
column = len(mat[0])
ans = 0
for i in range(1, min(line, column)+1):
    flag = False
    for j in range(0, line-i+1):
        for k in range(0, column-i+1):
            if sum_square(mat, j, k, i) <= threshold:
                flag = True
                ans += 1
                break
        if flag:
            break
    if not flag:
        break
print(ans)
