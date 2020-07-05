def func():
    arr_len, op_num = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    i = 0
    while i < op_num:
        op = input().split()
        if op[0] == "Q":
            temp = arr[int(op[1]) - 1:int(op[2])]
            temp.sort()
            print(temp[int(op[3]) - 1])
        else:
            arr[int(op[1]) - 1] = int(op[2])

        i += 1


func()
