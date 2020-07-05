test_num = int(input())
for test in range(0, test_num):
    row_width = int(input())
    matrix_0 = list(map(int, input().split()))
    matrix_1 = [[] for x in range(0, row_width)]
    for i in range(0, row_width):
        for j in range(0, row_width):
            matrix_1[i].append(matrix_0[i * row_width + j])
    result = []
    temp_ls = [x for x in range(0, row_width)]
    temp_ls.reverse()
    for i in range(0, row_width):
        for j in temp_ls:
            result.append(matrix_1[j][i])
    for i in range(0, len(result) - 1):
        print(result[i], end=" ")
    print(result[-1])