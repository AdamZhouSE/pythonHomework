def inc(matrix, op):
    i = 0
    while i < op[0] and i < len(matrix):
        j = 0
        while j < op[1] and j < len(matrix[0]):
            matrix[i][j] += 1
            j += 1
        i += 1


def func():
    rows_num = int(input())
    cols_num = int(input())

    matrix = [[0 for x in range(0, cols_num)] for y in range(0, rows_num)]

    op_num = int(input())
    i = 0
    while i < op_num:
        op = [int(x) for x in input().split(",")]
        inc(matrix, op)
        i += 1

    arr = []
    for ele in matrix:
        arr += ele

    max_count = arr.count(arr[0])

    print(max_count)


func()
