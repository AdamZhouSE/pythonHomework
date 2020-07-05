def func():
    rows_num = int(input())
    matrix = []
    i = 0
    while i < rows_num:
        matrix += [int(x) for x in input().split(",")]
        i += 1
    target = int(input())
    if target in matrix:
        print("True")
    else:
        print("False")


func()
