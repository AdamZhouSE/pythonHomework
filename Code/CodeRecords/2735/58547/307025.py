def func():
    arr_len, op_num = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    i = 0
    while i < op_num:
        op = [int(x) for x in input().split()]
        temp = arr[op[0] - 1:op[1]]
        temp.sort()
        print(temp[op[2] - 1])
        i += 1


func()
