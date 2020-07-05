def func():
    str_list = list(input())
    x = "no exist\n" + "".join(str_list)
    op_n = input().split()

    if len(op_n) == 2:
        if op_n[1] in str_list:
            str_list.remove(op_n[1])
        else:
            str_list = ["-1"]
    elif op_n[0] == "I":
        i = len(str_list) - 1
        flag = False  # found?
        while i > -1:
            if str_list[i] == op_n[1]:
                str_list.insert(i, op_n[2])
                flag = True
                break
            i -= 1
        if not flag:
            str_list = ["-1"]
    else:
        if op_n[1] in str_list:
            str_list = list("".join(str_list).replace(op_n[1], op_n[2]))
        else:
            str_list = ["-1"]

    if str_list == ["-1"]:
        print(x)
    else:
        print("".join(str_list))


func()
