test_num = int(input())
for test in range(0, test_num):
    row_width = int(input())
    matrix_0 = list(map(int, input().split()))
    matrix_1 = [[] for x in range(0, row_width)]
    for i in range(0, row_width):
        for j in range(0, row_width):
            matrix_1[i].append(matrix_0[i * row_width + j])
    print(matrix_0)
    print(matrix_1)