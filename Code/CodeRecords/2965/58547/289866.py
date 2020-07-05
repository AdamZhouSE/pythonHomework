def func():
    out_len = [int(x) for x in input().split()][0]
    string = input()
    op_num = int(input())

    i = 0
    while i < op_num:
        L, R, to_pos = [int(x) for x in input().split()]
        string = string[0: to_pos] + string[L: R] + string[to_pos:]
        i += 1

    print(string[:out_len], end="", flush=True)


func()
