test_num = input()
for i in test_num:
    unread = []
    read = []
    trash = []
    N, Q = input().split(" ")
    for j in range(int(N)):
        unread.append(str(j + 1))
    op_list = input().split(" ")
    for k in range(int(Q)):
        op_code = op_list[k * 2]
        op_num = op_list[k * 2 + 1]
        if op_code == "1":
            read.append(op_num)
            unread.remove(op_num)
        elif op_code == "2":
            trash.append(op_num)
            read.remove(op_num)
        elif op_code == "3":
            trash.append(op_num)
            unread.remove(op_num)
        elif op_code == "4":
            read.append(op_num)
            trash.remove(op_num)
    if len(unread) == 0:
        print("EMPTY")
    else:
        print(" ".join(unread) + " ")
    if len(read) == 0:
        print("EMPTY")
    else:
        print(" ".join(read) + " ")
    if len(trash) == 0:
        print("EMPTY")
    else:
        print(" ".join(trash) + " ")
