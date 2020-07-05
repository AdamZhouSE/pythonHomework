def func():
    arr = input()[1:-1].split(",")

    tree_dict = {1: [0]}  # depth: indexes of the depth
    now_depth = 1
    while True:
        flag = True
        tree_dict[now_depth + 1] = []
        for index in tree_dict[now_depth]:
            f1 = True
            f2 = True
            if index * 2 + 1 < len(arr) and arr[index * 2 + 1] != "null":
                tree_dict[now_depth + 1].append(index * 2 + 1)
                flag = False
                f1 = False
            if index * 2 + 2 < len(arr) and arr[index * 2 + 2] != "null":
                tree_dict[now_depth + 1].append(index * 2 + 2)
                flag = False
                f2 = False
            if f1 and f2:
                print(now_depth)
                return

        if flag:
            tree_dict.pop(now_depth + 1)
            # if now ele in list, pop out

        now_depth += 1


func()
